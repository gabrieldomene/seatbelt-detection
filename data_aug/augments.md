# Data augmentation in dataset

## INFO

* 526 images in total
* 403 labeled images
* 123 photoshopped removed seatbelt

### Augmentations

1. First set
   Pre-processing options:
      * Auto-adjust contrast -> Adaptive Equalization

   Augmentations per image -> 2
   
   Image level augmentations:
      * Flip horizontal
      * Brightness 25% dark and brighten
      * Exposure 25%
      * Noise 2%

2. Second set
   * Pre-processing options:
      * Auto-adjust contrast -> Adaptive Equalization

   Augmentations per image -> 1

   Image level augmentations:
      * Flip horizontal
      * Random rotation 5%
      * Random shear 20% both

3. Third set
   * Pre-processing options:
     * None

   Augmentations per image -> 3

   Image level augmentations:
     * Flip horizontal
     * Random rotation 5%
     * Random Shear 20%
     * Random crop 15%-25%
     * Blur 1px
     * Noise 2%
