# HIC-Yolov5

This repo contains the code for the HIC-YOLOv5, the original paper is:

> **HIC-YOLOv5: Improved YOLOv5 For Small Object Detection**<br>
> Shiyi Tang, Fang Yini, Shu Zhang<br>
> \[[Paper](https://arxiv.org/abs/2309.16393)\]

## To get started

### 1. Requirements

Run `pip install -r requirements.txt` in terminal.

### 2. Prepare Visdrone-2019 dataset 

(a) You can download the dataset from https://github.com/VisDrone/VisDrone-Dataset#task-1-object-detection-in-images.  

(b) Convert data form to Yolo by running `visDrone2yolov5.py` (you may need to change the `dir`).  

We suppose the data directory is constructed as
```
Your project name
├── datasets
|   ├── VisDrone2019
|   |   └── VisDrone2019-DET-train
            └── annotations
            └── images
            └── labels
|   |   └── VisDrone2019-DET-val
            └── annotations
            └── images
            └── labels
|   |   └── VisDrone2019-DET-test-dev
            └── annotations
            └── images
            └── labels
├── yolov5-6.0
```
(c) Modify path args in `data/VisDrone.yaml` . 

### 3. Train the model

Modify args in `train.py`. In HIC-Yolov5, some args are set as follows:

* `--weights`: `yolov5s.pt`
* `-cfg`: `models/yolov5s-p2-involution-cbam.yaml`
* `--hyp`: `data/hyps/hyp.scratch-high.yaml`

### 4. Evaluate the model

Modify args in `val.py`.

* `--weights`: the `best.pt` file in your result folder.
* `--task`: can be `val` or `test`.

## Cite

If you find this work useful in your research, please cite the paper:

```
@misc{tang2023hicyolov5,
      title={HIC-YOLOv5: Improved YOLOv5 For Small Object Detection}, 
      author={Shiyi Tang and Yini Fang and Shu Zhang},
      year={2023},
      eprint={2309.16393},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```

## Contact

My email: st2015@hw.ac.uk
