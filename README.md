run: python train.py --dataset deecamp --model deecamp --method maml --train_aug 

python test.py --dataset deecamp --model deecamp --method maml --train_aug

##matchingnet save_feature.py test.py

##io_utils.py: setting(CwayKshot) 

##method:
├── baselinefinetune.py
├── baselinetrain.py
├── __init__.py
├── maml.py
├── matchingnet.py
├── meta_template.py
├── protonet.py
└── relationnet.py

##backbone: conv,simpleblock,bottleblock

##train.py optimizer lr size 


# A Closer Look at Few-shot Classification

This repo contains the reference source code for the paper [A Closer Look at Few-shot Classification](https://openreview.net/pdf?id=HkxLXnAcFQ) in International Conference on Learning Representations (ICLR 2019). In this project, we provide a integrated testbed for a detailed empirical study for few-shot classification.


## Citation
If you find our code useful, please consider citing our work using the bibtex:
```
@inproceedings{
chen2019closerfewshot,
title={A Closer Look at Few-shot Classification},
author={Chen, Wei-Yu and Liu, Yen-Cheng and Kira, Zsolt and Wang, Yu-Chiang and  Huang, Jia-Bin},
booktitle={International Conference on Learning Representations},
year={2019}
}
```

## Enviroment
 - Python3
 - [Pytorch](http://pytorch.org/) before 0.4 (for newer vesion, please see issue #3 )
 - json

## Getting started
### CUB
* Change directory to `./filelists/CUB`
* run `source ./download_CUB.sh`

### mini-ImageNet
* Change directory to `./filelists/miniImagenet`
* run `source ./download_miniImagenet.sh` 

(WARNING: This would download the 155G ImageNet dataset. You can comment out correponded line 5-6 in `download_miniImagenet.sh` if you already have one.) 

### mini-ImageNet->CUB (cross)
* Finish preparation for CUB and mini-ImageNet and you are done!

### Omniglot
* Change directory to `./filelists/omniglot`
* run `source ./download_omniglot.sh` 

### Omniglot->EMNIST (cross_char)
* Finish preparation for omniglot first
* Change directory to `./filelists/emnist`
* run `source ./download_emnist.sh`  

### Self-defined setting
* Require three data split json file: 'base.json', 'val.json', 'novel.json' for each dataset  
* The format should follow   
{"label_names": ["class0","class1",...], "image_names": ["filepath1","filepath2",...],"image_labels":[l1,l2,l3,...]}  
See test.json for reference
* Put these file in the same folder and change data_dir['DATASETNAME'] in configs.py to the folder path  

## References
Our testbed builds upon several existing publicly available code. Specifically, we have modified and integrated the following code into this project:

* Framework, Backbone, Method: Matching Network
https://github.com/facebookresearch/low-shot-shrink-hallucinate 
* Omniglot dataset, Method: Prototypical Network
https://github.com/jakesnell/prototypical-networks
* Method: Relational Network
https://github.com/floodsung/LearningToCompare_FSL
* Method: MAML
https://github.com/cbfinn/maml  
https://github.com/dragen1860/MAML-Pytorch  
https://github.com/katerakelly/pytorch-maml
