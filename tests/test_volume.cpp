#include <gtest/gtest.h>
#include "volume.h"

TEST(VolumeControlTest, IncreasesNormally) {
    EXPECT_EQ(change_volume(20, 5), 25);
}

TEST(VolumeControlTest, ClampsAtMaxVolume) {
    EXPECT_EQ(change_volume(95, 10), MAX_VOLUME);
}

TEST(VolumeControlTest, ClampsAtMinVolume) {
    EXPECT_EQ(change_volume(5, -15), MIN_VOLUME);
}