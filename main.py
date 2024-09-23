import librosa
import madmom
from pydub import AudioSegment
import speech_recognition as sr
from essentia.standard import MonoLoader, RhythmExtractor2013

# Load Audio File
def load_audio_file(filepath):
    try:
        y, sr = librosa.load(filepath)
        return y, sr
    except Exception as e:
        print(f"Error loading file: {e}")
        return None, None

# Extract Tempo using Librosa
def extract_tempo(filepath):
    y, sr = load_audio_file(filepath)
    if y is not None:
        tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
        print(f"Estimated Tempo (BPM): {tempo}")
    else:
        print("Error extracting tempo")

# Extract Rhythm using Madmom
def extract_rhythm(filepath):
    try:
        proc = madmom.features.beats.RNNBeatProcessor()
        beats = proc(filepath)
        print(f"Beats detected at: {beats}")
    except Exception as e:
        print(f"Error extracting rhythm: {e}")

# Extract Duration using Pydub
def extract_duration(filepath):
    try:
        song = AudioSegment.from_file(filepath)
        duration_in_seconds = len(song) / 1000
        print(f"Duration: {duration_in_seconds} seconds")
    except Exception as e:
        print(f"Error extracting duration: {e}")

# Speech Recognition for Lyrics/Voice
def recognize_voice(filepath):
    r = sr.Recognizer()
    try:
        with sr.AudioFile(filepath) as source:
            audio = r.record(source)
            text = r.recognize_google(audio)
            print(f"Recognized speech: {text}")
    except Exception as e:
        print(f"Error recognizing voice: {e}")

# Rhythm Analysis using Essentia
def extract_essentia_rhythm(filepath):
    try:
        loader = MonoLoader(filename=filepath)
        audio = loader()
        rhythm_extractor = RhythmExtractor2013()
        bpm, beats, beats_confidence, _, _ = rhythm_extractor(audio)
        print(f"Essentia Estimated tempo: {bpm} BPM")
        print(f"Essentia Beat timings: {beats}")
    except Exception as e:
        print(f"Error using Essentia: {e}")

# Main Function to Perform Analysis
def analyze_audio(filepath):
    print(f"\nAnalyzing file: {filepath}\n")
    
    # Extract Tempo using Librosa
    print("Extracting Tempo...")
    extract_tempo(filepath)

    # Extract Rhythm using Madmom
    print("\nExtracting Rhythm...")
    extract_rhythm(filepath)

    # Extract Duration using Pydub
    print("\nExtracting Duration...")
    extract_duration(filepath)

    # Recognize Voice using SpeechRecognition
    print("\nRecognizing Voice...")
    recognize_voice(filepath)

    # Essentia Rhythm Analysis
    print("\nExtracting Rhythm with Essentia...")
    extract_essentia_rhythm(filepath)

if __name__ == "__main__":
    # Replace 'audio/song.mp3' with your actual file path
    analyze_audio('audio/song.mp3')