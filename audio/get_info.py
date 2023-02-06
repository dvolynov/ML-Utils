def get_info(track):
    return {
        "Длительность":                track.duration_seconds,
        "Количество каналов":          track.channels,
        "Размер семплов":              track.sample_width,
        "Частота дискретизации в кГц": track.frame_rate,
        "Размер фрейма":               track.frame_width,
        "Громкость в дБ":              track.rms,
        "Максимальная амплитуда":      track.max,
        "Максимальная амплитуда в дБ": track.max_dBFS,
    }