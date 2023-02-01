# COCO to YOLO format

It's a tool can help you convert COCO format to YOLO format.

By two steps:

1. Convert ``COCO.json`` to ``xml``
2. Convert ``xml`` to ``yolo.txt``

## Install

```bash
# Download the repo
git clone https://github.com/DanielHo-BS/coco2yolo.git
cd coco2yolo
# Install python library
pip install -r requirements.txt
```

## Usage

1. Create ``classes.txt`` with Classes which you want find.

    ```txt
    Text
    Table
    ......
    Title
    Footnote
    ```

2. Setting PATH in ``coco2xml.py``

    ```python
    COCO_ANNOTATIONS_PATH = '/COCO/train.json'
    COCO_IMAGES_DIRECTORY = '/PNG/'
    EXTRACTED_SAVING_PATH = '/train_coco_format/'
    CLASS_TXT = '/classes.txt' # Classes which you want to find
    ```

3. Setting PATH in ``xml2yolo.py``

    ```python
    #Setting relative path
    LABEL_PATH = '/train_coco_format/'           
    IMAGE_PATH = '/train_coco_format/'
    SAVE_PATH = '/train_yolo_format/'
    ```

4. Setting LABEL of classes in ``xml2yolo.py``

    ```python
    # Setting Label of Classse by Using dictionary
    status_dic = {
                'Text':0, 'Table':1, 'Picture':2,
                'Page-header':3, 'Page-footer':4
                }   
    ```

5. Run in termainal

    ```bash
    # First way:
    ./main.sh
    # Seconud way:
    python3 coco2xml.py
    python3 xml2yolo.py
    ```

6. See the result by ``drew_bbox.py``

    1. Setting PATH in ``drew_bbox.py``

        ```python
        imageFolder = "test_yolo_format/image/"
        labelFolder = "test_yolo_format/label/"
        ```

    2. Run in termainal

        ```bash
        python3 drew_bbox.py
        ```

### Warring

If get error when run ``./main.sh``:

```bash
chmod a+x main.sh
```

## Reference

1. [YOLO convert COCO format to YOLO format](https://hackmd.io/@jim93073/r1laqq0jF)