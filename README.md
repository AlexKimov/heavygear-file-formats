# About
Old Activision games file formats and tools.

## Games and formats

| №     | Game | Platform | Year | File extensions |
| :--- | :-- | :------ | :------ | :------ |
| 1 | Spycraft: The Great Game | PC | 1996  | .ast |
| 2 | Heavy Gear 1 | PC | 1997 | .map, .tex  |
| 3 | Heavy Gear 2 | PC | 1998  | .map, .zfs  |

## Templates

#### 010 Editor

| № | Template | Script (unpack) |  Description   |
| :-- | :------- | :------- | :-- |
|  **1**  | [AST.bt](https://github.com/AlexKimov/heavygear-file-formats/blob/master/templates/ATS.bt) |  [AST.bt](https://github.com/AlexKimov/heavygear-file-formats/blob/master/AST.bt) |  010Editor template for **PRJ** game archive* (Heavy Gear 1/2)  |
|  **2**  | [MAP.bt](https://github.com/AlexKimov/heavygear-file-formats/blob/master/templates/MAP.bt) |   |  010Editor template for **MAP** file (Heavy Gear 1/2)  |
|  **2**  | [PTJ.bt](https://github.com/AlexKimov/heavygear-file-formats/blob/master/templates/PTJ.bt) |   |  010Editor template for **PTJ** file (Heavy Gear 1)  |
|  **3**  | [TEX.bt](https://github.com/AlexKimov/heavygear-file-formats/blob/master/templates/TEX.bt) |   |  010Editor template for **TEX** files (Heavy Gear 1)  |
|  **4**  | [ZFS.bt](https://github.com/AlexKimov/heavygear-file-formats/blob/master/templates/ZFS.bt) |  [ZFS.bt](https://github.com/AlexKimov/heavygear-file-formats/blob/master/ZFS.bt) |  010Editor template for **ZFS** files (Heavy Gear 2)  |

    * file compressed with zlib compression

#### Kaitai Struct

| № | ksy |  Description   |
| :-- | :------- | :------- |
|  **1**  | [TEX.ksy](https://github.com/AlexKimov/heavygear-file-formats/blob/master/templates/TEX.ksy) | (Heavy Gear 1)  |


## Scripts

#### QuickBMS 

| № | .bat file | Script  | Description   |
| :-- | :------- | :-------  | :-- |
|  **1**  | [run_prj.bat](https://github.com/AlexKimov/heavygear-file-formats/blob/master/scripts/run_prj.bat) | [prj.bms](https://github.com/AlexKimov/heavygear-file-formats/blob/master/scripts/prj.bms)  | Quickbms script to unpack .prj files |
|  **1**  | [run_zfs.bat](https://github.com/AlexKimov/heavygear-file-formats/blob/master/scripts/run_zfs.bat) | [zfs.bms](https://github.com/AlexKimov/heavygear-file-formats/blob/master/scripts/zfs.bms)  | Quickbms script to unpack .zfs files |

#### Noesis

| № | Script  | Description   |
| :-- | :------- | :-------  |
|  **1**  | [fmt_tex_hg1.py](https://github.com/AlexKimov/heavygear-file-formats/blob/master/scripts/fmt_tex_hg1.py)  | script to open .tex files |
