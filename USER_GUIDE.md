# Lester – User Guide


## General functionalty

Lester is a tool for retro-style rotoscoping. Using a small set of user-provided clicks on the first frame of a video, Lester creates simplified, stylized masks (e.g., shirt, pants, skin, hat), colorizes them, applies pixelation/retro finishing, and automatically propagates them across the remaining frames of the video. In the future, tools for manually drawing on the frames will be included.

This guide walks you through the complete workflow.

---

## 1. Loading a Video or Image

The first step is to load a video (`.mp4`) or a still image (`.jpg`, `.png`) through the **File** menu.



![screenshot-load-video](screenshot01.png)

After loading the video, a message may appear suggesting that you subsample the video to reduce its number of frames. This is important because mask propagation is computationally expensive. If the video has more than 100 frames, the message will warn you.



![screenshot-load-video](screenshot01.png)

After loading the video, a message may appear suggesting that you subsample the video to reduce its number of frames. This is important because mask propagation is computationally expensive. If the video has more than 100 frames, the message will warn you.

![screenshot-subsample-warning](screenshot02.png)

---

## 2. Optional: Subsample the Video

After loading the video, you can optionally reduce the number of frames by clicking the **Subsample video** button on the left panel.

![screenshot-subsample-button](screenshot03.png)

Subsampling the video makes the mask propagation step significantly faster. However:

- The resulting animation will also play faster (because frames were removed), making it look unrealistic.  
- Although you can add interpolated frames later to slow the animation down again, this interpolation feature is still experimental and does not work very well yet.

**Therefore, do not subsample unless your hardware is slow or the video is too long/complex for reasonable propagation time.**

---

## 3. Selecting Masks (Defining Regions on the First Frame)

The central panel shows the currently selected frame of the video.  
This is where you define *masks*, which correspond to regions of the frame.

There are two mask selection modes:

### 3.1. Click-to-Mask Mode (Default)

In the default mode, a mask is selected simply by clicking on the region you want to mask.

![screenshot-click-to-mask](screenshot04.png)

- Clicking once creates a mask.  
- Clicking again on the same mask deselects it.

This mode is the fastest and works well for clean, contiguous regions.

---

### 3.2. Multi-Point Mask Mode (+ / –)

You can activate a second mask selection mode by clicking the **+** or **–** radio buttons.  
This mode allows defining a mask using multiple positive or negative points:

- **Positive points** → belong to the mask  
- **Negative points** → explicitly do *not* belong to the mask  

After placing all desired points, click the **Mask** button to generate the mask.

![screenshot-multipoint-mask](screenshot05.png)

This mode is useful for:

- More complex masks  
- Masks composed of discontinuous regions (e.g., the visible skin of a character)

In theory, these masks can also be deselected using a single click when in click-to-mask mode, but sometimes this may fail.  
If you need to delete a mask reliably, use the **–** button in the masks list panel (bottom-left).

---

## 4. Editing Masks: Colors and Stacking Order

Once you have created your masks, you can edit them in the **masks list panel** (bottom-left).

### 4.1. Changing Mask Colors

You can change the color of each mask using:

- The color picker  
- The **P** button, which offers predefined classic palette colors  

![screenshot-mask-colors](screenshot06.png)

### 4.2. Changing Mask Stacking Order

Use the up/down arrows in the masks list to reorder the masks.  
This is important if some regions overlap visually.

![screenshot-mask-order](screenshot07.png)

---

## 5. Previewing Finishing Effects on the First Frame

On the right panel, you can preview the rotoscoped frame with the current settings applied.

At the bottom right (Finishing Details panel), you will find sliders for:

- **Rimlight size**  
- **Pixelation level**

![screenshot-finishing-details](screenshot08.png)

You can freely adjust these values now or later—after mask propagation—since finishing effects apply to all frames consistently.

---

## 6. Optional: Adding Facial Features

If your video includes a **frontal face** that is **clearly visible**, you can enable facial features:

- Checkbox: **Facial traits**  
- Color pickers: **Face color** and **Eyes color**

![screenshot-facial-traits](screenshot09.png)

This feature only works when the face is frontal and unobstructed.  
Lester will attempt to propagate facial traits automatically along with the masks.

---

## 7. Propagating Masks to the Whole Video

Once your masks and finishing settings are ready, click:

**Left panel → Propagate masks**

![screenshot-propagate-masks](screenshot10.png)

The system will ask to which frame you want to propagate.  
Propagation may take from several seconds to several minutes depending on:

- The number of frames  
- The number of masks  
- The complexity of the regions  
- Your hardware performance  

This process also propagates facial traits if they were enabled.

---

## 8. Viewing the Resulting Animation

After propagation completes, you can view the processed frames in the right panel.  
You can also play the resulting animation with the playback controls (play, reset, loop, navigation bar).

![screenshot-playback](screenshot11.png)

---

## 9. Saving Your Animation

Finally, you can save the animation either as:

- An `.mp4` video  
- A set of `.png` frames

![screenshot-save-dialog](screenshot12.png)

Saving as `.png` frames will preserve transparency and is the recommended option if you intend to create:

- Videogame animations  
- Animated GIFs  
- Further composited artwork

### Interpolation Option

When saving, Lester will ask whether you want to apply interpolation.  
This is primarily intended for videos that were subsampled earlier.  
However, this feature is still not very reliable, so use it cautiously.

---

## Summary

- Load your video → optionally subsample  
- Create masks on the first frame using click-to-mask or multi-point mode  
- Adjust mask colors and stacking order  
- Set finishing details (rimlight, pixelation)  
- Optionally enable facial features (frontal faces only)  
- Propagate masks to the whole video  
- Preview and export the animation (MP4 or PNG frames)

More editing features will be added in future versions of Lester.

