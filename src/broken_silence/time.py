class Time:
    FACTORS = 60, 60, 24, 1
    NAMES = "seconds", "minutes", "hours", "days"

    @classmethod
    def parse(cls, dur: str):
        parts = dur.split(":")
        parts.reverse()

        result = 0.0
        scale = 1

        for factor, part in zip(cls.FACTORS, parts):
            result += float(part) * scale
            scale *= factor

        return result

    @classmethod
    def format(cls, dur: float, show_zeros: bool = False):
        result = ""

        for factors in cls.FACTORS[:-1]:
            result = f"{dur % factors:02}:{result}"
            dur = int(dur / factors)

            if not show_zeros and dur == 0:
                break

        if show_zeros or dur != 0:
            result = f"{dur:02}:{result}"

        return result[:-1]

    @classmethod
    def max_time(cls, dur: float):
        parts = cls.format(dur).split(":")
        part = parts[0]

        name = cls.NAMES[min(len(parts), len(cls.NAMES)) - 1]
        if int(part) == 1:
            name = name[:-1]

        return f"{int(part)} {name}"
