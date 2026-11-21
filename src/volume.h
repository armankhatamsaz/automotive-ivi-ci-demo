#ifndef VOLUME_H
#define VOLUME_H

#ifdef __cplusplus
extern "C" {
#endif

#define MAX_VOLUME 100
#define MIN_VOLUME 0

int clamp_volume(int level);
int change_volume(int current, int delta);

#ifdef __cplusplus
}
#endif

#endif