import librosa
import numpy as np

def get_features(x, sr):
    chroma_stft = librosa.feature.chroma_stft(x, sr=sr)
    mfcc = librosa.feature.mfcc(x, sr=sr)

    rmse = np.mean(librosa.feature.rms(x))
    spec_cent = np.mean(librosa.feature.spectral_centroid(x, sr=sr))
    spec_bw = np.mean(librosa.feature.spectral_bandwidth(x, sr=sr))
    rolloff = np.mean(librosa.feature.spectral_rolloff(x, sr=sr))
    zcr = np.mean(librosa.feature.zero_crossing_rate(x))

    out = []
    out.append(rmse)
    out.append(spec_cent)
    out.append(spec_bw)
    out.append(rolloff)
    out.append(zcr)

    for e in mfcc:
        out.append(np.mean(e))

    for e in chroma_stft:
        out.append(np.mean(e))

    return out