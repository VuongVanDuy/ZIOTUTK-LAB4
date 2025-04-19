import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt
import librosa

class GeneratorNoise:
    def __init__(self, voices_path: list[str], fs: int | None, volume_voice: float, volume_noise: float):
        self.voices_path = voices_path
        self.fs = fs
        self.volume_voice = volume_voice
        self.volume_noise = volume_noise
        self.voices = []
        self.noise = None

    # Hàm tạo tiếng ồn trắng
    def generate_white_noise(self, num_samples ):
        return np.random.randn(num_samples)

    def normalize_signal(self, signal_array: np.ndarray) -> np.ndarray:
        max_val = np.max(np.abs(signal_array))
        if max_val > 0:
            return signal_array / max_val
        return signal_array

    # đọc file âm thanh
    def read_voices(self, normalize_flag=True):
        # Đọc file âm thanh (giữ nguyên sample rate gốc)
        for voice_path in self.voices_path:
            voice, sr = librosa.load(voice_path, sr=self.fs)
            voice = voice * self.volume_voice
            if normalize_flag:
                voice = self.normalize_signal(voice)
            self.voices.append((voice, sr))

    def save_to_file(self, filename: str, signal_array: np.ndarray):
        """
        Сохраняет сигнал в файл WAV.
        """
        try:
            sf.write(filename, signal_array, self.fs)
            print(f"Saved generated noise to '{filename}'")
        except Exception as e:
            print(f"Error saving file: {e}")

    # tạo tiếng ồn bằng cách cộng tiếng ồn trắng và tiếng nói trong voices
    def generate(self):
        # Create white noise
        self.read_voices()
        if not self.fs:
            # If fs is not set, use the sample rate of the first voice
            self.fs = self.voices[0][1]
        max_length = max(len(voice) for voice, _ in self.voices)
        white_noise = self.generate_white_noise(num_samples=max_length)
        result = white_noise * self.volume_noise

        for voice, sr in self.voices:
            # Adjust voice signal length to match white noise
            if len(voice) > max_length:
                voice_adj = voice[:max_length]
            elif len(voice) < max_length:
                voice_adj = np.pad(voice, (0, max_length - len(voice)), mode='constant')
            else:
                voice_adj = voice
            result += voice_adj

        # Normalize the result
        result = self.normalize_signal(result)
        self.noise = result

    def compute_fft(self, signal_array, dt):
        N = len(signal_array)
        X = np.fft.fft(signal_array) * dt  # масштабирование для приближения интеграла
        freq = np.fft.fftfreq(N, d=dt)
        # Сдвигаем нулевую частоту к центру
        X_shift = np.fft.fftshift(X)
        freq_shift = np.fft.fftshift(freq)

        return freq_shift, np.abs(X_shift)

    def amplitude_spectrum(self):
        dt = 1 / self.fs
        freq, X = self.compute_fft(self.noise, dt)
        plt.figure()
        plt.plot(freq, X)
        plt.xlim(0, self.fs / 2)
        plt.xlabel('Frequency [Hz]')
        plt.ylabel('Amplitude')
        plt.title('Amplitude Spectrum')
        plt.tight_layout()
        plt.show()

    def compare_with_user_voice(self, voice_file='my_voice.wav'):
        # Read voice file
        voice, sr = librosa.load(voice_file, sr=None)
        # Normalize both signals
        noise = self.normalize_signal(self.noise)
        voice = self.normalize_signal(voice)

        # Compute FFT for both signals
        dt_noise = 1 / self.fs
        freq_noise, X_noise = self.compute_fft(noise, dt_noise)
        dt_voice = 1 / sr
        freq_voice, X_voice = self.compute_fft(voice, dt_voice)

        # Plotting
        plt.figure(figsize=(12, 6))
        plt.subplot(2, 1, 1)
        plt.plot(freq_noise, X_noise)
        plt.xlim(0, self.fs / 2)
        plt.xlabel('Frequency [Hz]')
        plt.ylabel('Amplitude')
        plt.title('Amplitude Spectrum of Generated Noise')

        plt.subplot(2, 1, 2)
        plt.plot(freq_voice, X_voice)
        plt.xlim(0, sr / 2)
        plt.xlabel('Frequency [Hz]')
        plt.ylabel('Amplitude')
        plt.title('Amplitude Spectrum of Voice')

        plt.tight_layout()
        # save the plot
        plt.show()

