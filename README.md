# Lester: Rotoscope Animation Through Video Object Segmentation and Tracking

## 1. Introduction

This repository contains information, code and data related to the Lester project. The project aims at developing a sytem capable of  automatically synthetise retro-style 2D animations from videos.

<!--![](/data/test1/result_dual.gif)-->

<p float="center">
  <img src="img/output.gif" width="200" />
</p>




<!--
## 2 Acknowledgements

If you find this repository useful for your research, please cite the original publication:

	TODO


## 2 Preliminar tests

- Scene 1 
	- [input video](/data/topgun/footage.mp4?raw=true)
	- [3D character](/data/topgun/obj)
-->

## 2. Pictonaut dataset of film shots

### 2.1 Input videos and 3D characters

- Scene 1 (Top Gun)
	- [input video](/data/topgun/footage.mp4?raw=true)
	- [3D character](/data/topgun/obj)
- Scene 2 (Paris Texas)
	- [input video](/data/paristexas/footage.mp4?raw=true)
	- [3D character](/data/paristexas/obj)
- Scene 3 (Terminator)
	- [input video](/data/terminator/footage.mp4?raw=true)
	- [3D character](/data/terminator/obj)
- Scene 4 (Alien)
	- [input video](/data/alien/footage.mp4?raw=true)
	- [3D character](/data/alien/obj)
- Scene 5 (Night of the Living Dead 1/6)
	- [input video](/data/night1/footage.mp4?raw=true)
	- [3D character](/data/night1/obj)
- Scene 6 (Night of the Living Dead 2/6)
	- [input video](/data/night2/footage.mp4?raw=true)
	- [3D character](/data/night2/obj)
- Scene 7 (Night of the Living Dead 3/6)
	- [input video](/data/night3/footage.mp4?raw=true)
	- [3D character](/data/night3/obj)
- Scene 8 (Night of the Living Dead 4/6)
	- [input video](/data/night4/footage.mp4?raw=true)
	- [3D character](/data/night4/obj)
- Scene 9 (Night of the Living Dead 5/6)
	- [input video](/data/night5/footage.mp4?raw=true)
	- [3D character](/data/night5/obj)
- Scene 10 (Night of the Living Dead 6/6)
	- [input video](/data/night6/footage.mp4?raw=true)
	- [3D character](/data/night6/obj)
- Scene 11 (Charade 1/3)
	- [input video](/data/charade1/footage.mp4?raw=true)
	- [3D character](/data/charade1/obj)
- Scene 12 (Charade 2/3)
	- [input video](/data/charade2/footage.mp4?raw=true)
	- [3D character](/data/charade2/obj)
- Scene 13 (Charade 3/3)
	- [input video](/data/charade3/footage.mp4?raw=true)
	- [3D character](/data/charade3/obj)

### 2.2 Results

- Scene 1 (Top Gun)
	- [result](/data/topgun/result.mp4?raw=true)
	- [result dual](/data/topgun/result_dual.mp4?raw=true)
	- [comparative result with CartoonGAN](/data/topgun/cartoongan.mp4?raw=true)
- Scene 2 (Paris Texas)
	- [result](/data/paristexas/result.mp4?raw=true)
	- [result dual](/data/paristexas/result_dual.mp4?raw=true)
	- [comparative result with CartoonGAN](/data/paristexas/cartoongan.mp4?raw=true)
- Scene 3 (Terminator)
	- [result](/data/terminator/result.mp4?raw=true)
	- [result dual](/data/terminator/result_dual.mp4?raw=true)
	- [comparative result with CartoonGAN](/data/terminator/cartoongan.mp4?raw=true)
- Scene 4 (Alien)
	- [result](/data/alien/result_dual.mp4?raw=true)
	- [result dual](/data/alien/result.mp4?raw=true)
	- [comparative result with CartoonGAN](/data/alien/cartoongan.mp4?raw=true)
- Scene 5 (Night of the Living Dead 1/6)
	- [result](/data/night1/result.mp4?raw=true)
	- [comparative result with CartoonGAN](/data/night1/cartoongan.mp4?raw=true)
- Scene 6 (Night of the Living Dead 2/6)
	- [result](/data/night2/result.mp4?raw=true)
- Scene 7 (Night of the Living Dead 3/6)
	- [result](/data/night3/result.mp4?raw=true)
- Scene 8 (Night of the Living Dead 4/6)
	- [result](/data/night4/result.mp4?raw=true)
- Scene 9 (Night of the Living Dead 5/6)
	- [result](/data/night5/result.mp4?raw=true)
- Scene 10 (Night of the Living Dead 6/6)
	- [result](/data/night6/result.mp4?raw=true)
- Scene 11 (Charade 1/3)
	- [result](/data/charade1/result.mp4?raw=true)
- Scene 12 (Charade 2/3)
	- [result](/data/charade2/result.mp4?raw=true)
- Scene 13 (Charade 3/3)
	- [result](/data/charade3/result.mp4?raw=true)

## 3. Pictonaut result over CMU Motion Capture dataset

<p float="center">
  <img src="/data/cmu_17_10/result.gif" width="400" />
</p>

- Subject 17 / Motion 10
	- [input video](/data/cmu_17_10/footage.mp4?raw=true)
	- [result](/data/cmu_17_10/result.mp4?raw=true)

- Subject 8 / Motion 10
	- [input video](/data/cmu_08_10/footage.mp4?raw=true)
	- [result](/data/cmu_08_10/result.mp4?raw=true)

- Subject 35 / Motion 17
	- [input video](/data/cmu_35_17/footage.mp4?raw=true)
	- [result](/data/cmu_35_17/result.mp4?raw=true)

- Subject 9 / Motion 1
	- [input video](/data/cmu_09_01/footage.mp4?raw=true)
	- [result](/data/cmu_09_01/result.mp4?raw=true)

- Subject 2 / Motion 5
	- [input video](/data/cmu_02_05/footage.mp4?raw=true)
	- [result](/data/cmu_02_05/result.mp4?raw=true)

## 4. Pictonaut result over Human3.6M dataset

- Subject 2 / Posing 1
	- [input video](/data/h36m_s2_1/footage.mp4?raw=true)
	- [result](/data/h36m_s2_1/result.mp4?raw=true)

- Subject 5 / Posing 1
	- [input video](/data/h36m_s5_1/footage.mp4?raw=true)
	- [result](/data/h36m_s5_1/result.mp4?raw=true)

- Subject 5 / Posing 4
	- [input video](/data/h36m_s5_4/footage.mp4?raw=true)
	- [result](/data/h36m_s5_4/result.mp4?raw=true)

- Subject 7 / Posing 1
	- [input video](/data/h36m_s7_1/footage.mp4?raw=true)
	- [result](/data/h36m_s7_1/result.mp4?raw=true)

- Subject 7 / Posing 2
	- [input video](/data/h36m_s7_2/footage.mp4?raw=true)
	- [result](/data/h36m_s7_2/result.mp4?raw=true)

- Subject 7 / Posing 3
	- [input video](/data/h36m_s7_3/footage.mp4?raw=true)
	- [result](/data/h36m_s7_3/result.mp4?raw=true)

- Subject 7 / Posing 4
	- [input video](/data/h36m_s7_4/footage.mp4?raw=true)
	- [result](/data/h36m_s7_4/result.mp4?raw=true)

- Subject 7 / Posing 5
	- [input video](/data/h36m_s7_5/footage.mp4?raw=true)
	- [result](/data/h36m_s7_5/result.mp4?raw=true)

- Subject 8 / Posing 1
	- [input video](/data/h36m_s8_1/footage.mp4?raw=true)
	- [result](/data/h36m_s8_1/result.mp4?raw=true)

- Subject 8 / Posing 2
	- [input video](/data/h36m_s8_2/footage.mp4?raw=true)
	- [result](/data/h36m_s8_2/result.mp4?raw=true)