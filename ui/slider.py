from pygame import *

class Slider:
    def __init__(self, x, y, width, min_val, max_val, step=1, initial=None, label="", value_to_text=None):
        self.track_rect = Rect(x, y, width, 6)
        self.handle_radius = 10
        self.min = float(min_val)
        self.max = float(max_val)
        if initial is not None:
            self.value = float(initial)
        else:
            self.value = float(min_val)
        self.label = label
        self.value_to_text = value_to_text
        self.dragging = False
        self._hit_rect = Rect(0, 0, self.handle_radius * 2, self.handle_radius * 2)

    def _clamp(self, v: float) -> float:
        pass