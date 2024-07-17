# Lester: Rotoscope Animation Through Video Object Segmentation and Tracking

## 1. Introduction

This repository contains data related to the Lester project. The project aims at developing a sytem capable of  automatically synthetise retro-style 2D animations from videos. Another repository, [rtous/lester-code](https://github.com/rtous/lester-code) contains the code.

<!--![](/data/test1/result_dual.gif)-->

<p align="center">
  <img src="img/out.gif" width="200" />
</p>


## 2 Acknowledgements

If you find this repository useful for your research, please cite the original publication:

	@misc{rtous2024lester,
	  title={Lester: Rotoscope Animation Through Video Object Segmentation and Tracking},
	  author={Ruben Tous},
	  eprint={2402.09883},
	  archivePrefix={arXiv},
	  primaryClass={cs.CV},
	  url={https://arxiv.org/abs/2402.09883},
	  year={2024}
	}

## 3. Results

YouTube videos:

- Video 1
	- Id: youtube1
	- Source: YouTube
	- [input](/results/youtube1/footage.mp4?raw=true)
	- [result](/results/youtube1/out_final.mp4?raw=true)

<p align="center">
  <img src="/results/youtube1/out.gif" width="200" />
</p>

- Video 2
	- Id: youtube2
	- Source: YouTube
	- [input](/results/youtube2/footage.mp4?raw=true)
	- [result](/results/youtube2/out_final.mp4?raw=true)

<p align="center">
  <img src="/results/youtube2/out.gif" width="200" />
</p>

- Video 3
	- Id: youtube3
	- Source: YouTube
	- [input](/results/youtube3/footage.mp4?raw=true)
	- [result](/results/youtube3/out_final.mp4?raw=true)
	- [result fine-tuned Stable Diffusion + ControlNet + EbSynth](/results/youtube3/sd_lester.mp4?raw=true)

<p align="center">
  <img src="/results/youtube3/out.gif" width="200" />
</p>

- Video 4
	- Id: youtube4
	- Source: YouTube
	- [input](/results/youtube4/footage.mp4?raw=true)
	- [result](/results/youtube4/out_final.mp4?raw=true)

<p align="center">
  <img src="/results/youtube4/out.gif" width="200" />
</p>

- Video 5
	- Id: youtube5
	- Source: YouTube
	- [input](/results/youtube5/footage.mp4?raw=true)
	- [result](/results/youtube5/out_final.mp4?raw=true)

<p align="center">
  <img src="/results/youtube5/out.gif" width="200" />
</p>

- Video 6
	- Id: youtube6
	- Source: YouTube
	- [input](/results/youtube6/footage.mp4?raw=true)
	- [result](/results/youtube6/out_final.mp4?raw=true)

<p align="center">
  <img src="/results/youtube6/out.gif" width="200" />
</p>

- Video 7
	- Id: youtube7
	- Source: YouTube
	- [input](/results/youtube7/footage.mp4?raw=true)
	- [result](/results/youtube7/out_final.mp4?raw=true)
	- [result fine-tuned Stable Diffusion + ControlNet + EbSynth](/results/youtube7/sd_lester.mp4?raw=true)

<p align="center">
  <img src="/results/youtube7/out.gif" width="100" />
</p>

- Video 8
	- Id: youtube8
	- Source: YouTube
	- [input](/results/youtube8/footage.mp4?raw=true)
	- [result](/results/youtube8/out_final.mp4?raw=true)

<p align="center">
  <img src="/results/youtube8/out.gif" width="200" />
</p>

- Video 9
	- Id: youtube9
	- Source: YouTube
	- [input](/results/youtube9/footage.mp4?raw=true)
	- [result](/results/youtube9/out_final.mp4?raw=true)

<p align="center">
  <img src="/results/youtube9/out.gif" width="200" />
</p>

- Video 10
	- Id: youtube10
	- Source: YouTube
	- [input](/results/youtube10/footage.mp4?raw=true)
	- [result](/results/youtube10/out_final.mp4?raw=true)

<p align="center">
  <img src="/results/youtube10/out.gif" width="200" />
</p>

Videos from the Fashion Video Dataset of the CV Lab of the University of British Columbia:

- Video 11
	- Id: fvd_1
	- Source: test/91oFLFG8UNS.mp4 
	- [input](/results/fvd1/footage.mp4?raw=true)
	- [result](/results/fvd1/out_final.mp4?raw=true)

<p align="center">
  <img src="/results/fvd1/out.gif" width="100" />
</p>

- Video 12
	- Id: fvd_2
	- Source: test/91uY9usoa5S.mp4
	- [input](/results/fvd2/footage.mp4?raw=true)
	- [result](/results/fvd2/out_final.mp4?raw=true)

<p align="center">
  <img src="/results/fvd2/out.gif" width="100" />
</p>

- Video 13
	- Id: fvd_3
	- Source: test/A1gga724uoS.mp4
	- [input](/results/fvd3/footage.mp4?raw=true)
	- [result](/results/fvd3/out_final.mp4?raw=true)

<p align="center">
  <img src="/results/fvd3/out.gif" width="100" />
</p>

- Video 14
	- Id: fvd_4
	- Source: test/A1rJWpLlTwS.mp4
	- [input](/results/fvd4/footage.mp4?raw=true)
	- [result](/results/fvd4/out_final.mp4?raw=true)

<p align="center">
  <img src="/results/fvd4/out.gif" width="100" />
</p>

- Video 15
	- Id: fvd_5
	- Source: test/A1VF4yftLZS.mp4
	- [input](/results/fvd5/footage.mp4?raw=true)
	- [result](/results/fvd5/out_final.mp4?raw=true)

<p align="center">
  <img src="/results/fvd5/out.gif" width="100" />
</p>

Videos from the UCF101 Human Actions dataset:

- Video 16
	- Id: ucf101_1
	- Source: UCF101/v_WallPushups_g01_c03.avi
	- [input](/results/ucf101_1/footage.mp4?raw=true)
	- [result](/results/ucf101_1/out_final.mp4?raw=true)

<p align="center">
  <img src="/results/ucf101_1/out.gif" width="200" />
</p>

- Video 17
	- Id: ucf101_2
	- Source: UCF101/v_PizzaTossing_g05_c01.avi
	- [input](/results/ucf101_2/footage.mp4?raw=true)
	- [result](/results/ucf101_2/out_final.mp4?raw=true)

<p align="center">
  <img src="/results/ucf101_2/out.gif" width="200" />
</p>

- Video 18
	- Id: ucf101_3
	- Source: UCF101/v_BodyWeightSquats_g12_c01.avi
	- [input](/results/ucf101_3/footage.mp4?raw=true)
	- [result](/results/ucf101_3/out_final.mp4?raw=true)


<p align="center">
  <img src="/results/ucf101_3/out.gif" width="200" />
</p>

- Video 19
	- Id: ucf101_4
	- Source: UCF101/v_BodyWeightSquats_g20_c01.avi
	- [input](/results/ucf101_4/footage.mp4?raw=true)
	- [result](/results/ucf101_4/out_final.mp4?raw=true)

<p align="center">
  <img src="/results/ucf101_4/out.gif" width="200" />
</p>

- Video 20
	- Id: ucf101_5
	- Source: UCF101/v_BodyWeightSquats_g20_c01.avi
	- [input](/results/ucf101_5/footage.mp4?raw=true)
	- [result](/results/ucf101_5/out_final.mp4?raw=true)

<p align="center">
  <img src="/results/ucf101_5/out.gif" width="200" />
</p>

Videos from the Kinetics dataset:

- Video 21
	- Id: kinetics1
	- Source: U8LA_hHPISg_000102_000112.mp4
	- [input](/results/kinetics1/footage.mp4?raw=true)
	- [result](/results/kinetics1/out_final.mp4?raw=true)

<p align="center">
  <img src="/results/kinetics1/out.gif" width="200" />
</p>

- Video 22
	- Id: kinetics2
	- Source: zxsSfO4cHRQ_000000_000010.mp4
	- [input](/results/kinetics2/footage.mp4?raw=true)
	- [result](/results/kinetics2/out_final.mp4?raw=true)

<p align="center">
  <img src="/results/kinetics2/out.gif" width="200" />
</p>

- Video 23
	- Id: kinetics3
	- Source: yGA9OkTvvVM_000065_000075.mp4
	- [input](/results/kinetics3/footage.mp4?raw=true)
	- [result](/results/kinetics3/out_final.mp4?raw=true)


<p align="center">
  <img src="/results/kinetics3/out.gif" width="200" />
</p>

- Video 24
	- Id: kinetics4
	- Source: xkp3fD8HL68_000000_000010.mp4
	- [input](/results/kinetics4/footage.mp4?raw=true)
	- [result](/results/kinetics4/out_final.mp4?raw=true)
	- [result fine-tuned Stable Diffusion + ControlNet + EbSynth](/results/kinetics4/sd_lester.mp4?raw=true)

<p align="center">
  <img src="/results/kinetics4/out.gif" width="200" />
</p>

- Video 25
	- Id: kinetics5
	- Source: vg9Tg1gihmk_000015_000025.mp4
	- [input](/results/kinetics5/footage.mp4?raw=true)
	- [result](/results/kinetics5/out_final.mp4?raw=true)
	

<p align="center">
  <img src="/results/kinetics5/out.gif" width="200" />
</p>


