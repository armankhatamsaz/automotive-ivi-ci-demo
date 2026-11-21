#include "volume.h"

int clamp_volume(int level) {
    if (level > MAX_VOLUME) {
        return MAX_VOLUME;
    }
    if (level < MIN_VOLUME) {
        return MIN_VOLUME;
    }
    return level;
}

int change_volume(int current, int delta) {
    return clamp_volume(current + delta);
}
