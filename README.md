# About
Old Activision games file formats and tools.

## Games and formats

| №     | Game | Platform | Year | File extensions |
| :--- | :-- | :------ | :------ | :------ |
| 1 | Star Trek Armada | PC | 2000  | .zfs |
| 2 | Call to Power 2 | PC | 2000  | .zfs |
| 3 | Interstate '82 | PC | 1999  | .zfs |
| 4 | Civilization: Call to Power | PC | 1999  | .zfs |
| 5 | Battlezone | PC | 1998  | .zfs |
| 6 | Heavy Gear 2 | PC | 1998  | .map, .zfs, .prj  |
| 7 | Interstate '76 | PC | 1997 | .zfs |
| 8 | Zork: Grand Inquisitor | PC | 1997 | .zfs |
| 9 | Heavy Gear 1 | PC | 1997 | .map, .tex, .prj  |
| 10 | Spycraft: The Great Game | PC | 1996  | .ast |
| 11 | MechWarrior 2 / Titanium | PC | 1995/1998  | .sfl, .mw2, .prj  |

## Templates

#### 010 Editor

| № | Template | Script (unpack) | Game | Format description   |
| :-- | :------- | :------- | :-- | :-- |
|  **1**  | [ATS.bt](https://github.com/AlexKimov/heavygear-file-formats/blob/master/templates/ATS.bt) |  | Spycraft | Texture |
|  **2**  | [MW2.bt](https://github.com/AlexKimov/heavygear-file-formats/blob/master/templates/MW2.bt) |  | MechWarrior 2  | Archive  |
|  **3**  | [MAP.bt](https://github.com/AlexKimov/heavygear-file-formats/blob/master/templates/MAP.bt) |  |  Heavy Gear 1/2 | .prj archive filenames  |
|  **4**  | [PRJ.bt](https://github.com/AlexKimov/heavygear-file-formats/blob/master/templates/PRJ(HG1).bt) | [prj(hg1).bms](https://github.com/AlexKimov/heavygear-file-formats/blob/master/prj.bms)  |  | Heavy Gear 1 | Archive |
|  **5**  | [PRJ.bt](https://github.com/AlexKimov/heavygear-file-formats/blob/master/templates/PRJ(MW2).bt) | [prj(mw2).bms](https://github.com/AlexKimov/heavygear-file-formats/blob/master/prj.bms)  |  | MechWarrior 2 | Archive |
|  **6**  | [TEX.bt](https://github.com/AlexKimov/heavygear-file-formats/blob/master/templates/TEX.bt) |   | Heavy Gear 1  | Texture  |
|  **7**  | [SFL.bt](https://github.com/AlexKimov/heavygear-file-formats/blob/master/templates/SFL.bt) |   | MechWarrior 2 | Sound file |
|  **8**  | [SHP.bt](https://github.com/AlexKimov/heavygear-file-formats/blob/master/templates/SHP.bt) |   | MechWarrior 2 | Texture |
|  **9**  | [ZFS.bt](https://github.com/AlexKimov/heavygear-file-formats/blob/master/templates/ZFS.bt) |  [zfs.bms](https://github.com/AlexKimov/heavygear-file-formats/blob/master/scripts/zfs.bms) |  | Almost all | Archive  |


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
