from flask import Flask, request, jsonify
import librosa
import numpy as np

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        # Load audio file using librosa
        try:
            y, sr = librosa.load(file, sr=None)
            # For example, return the amplitude array
            data = y.tolist()
            # Set the hop length; at 22050 Hz, 512 samples ~= 23ms
            hop_length = 512

            # Separate harmonics and percussives into two waveforms
            y_harmonic, y_percussive = librosa.effects.hpss(y)

            # Beat track on the percussive signal
            tempo, beat_frames = librosa.beat.beat_track(y=y_percussive,
                                                        sr=sr)

            # Compute MFCC features from the raw signal
            mfcc = librosa.feature.mfcc(y=y, sr=sr, hop_length=hop_length, n_mfcc=13)

            # And the first-order differences (delta features)
            mfcc_delta = librosa.feature.delta(mfcc)

            # Stack and synchronize between beat events
            # This time, we'll use the mean value (default) instead of median
            beat_mfcc_delta = librosa.util.sync(np.vstack([mfcc, mfcc_delta]),
                                                beat_frames)

            # Compute chroma features from the harmonic signal
            chromagram = librosa.feature.chroma_cqt(y=y_harmonic,
                                                    sr=sr)

            # Aggregate chroma features between beat events
            # We'll use the median value of each feature between beat frames
            beat_chroma = librosa.util.sync(chromagram,
                                            beat_frames,
                                            aggregate=np.median)

            # Finally, stack all beat-synchronous features together
            beat_features = np.vstack([beat_chroma, beat_mfcc_delta])
            return jsonify({'audio_data': data, 'tempo' : tempo,'sampling_rate': sr, 'beat_features': beat_features.tolist()}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    return jsonify({'error': 'Unknown error'}), 400

if __name__ == '__main__':
    app.run(debug=True)

