meta:
    id: tex
    file-extension: tex
    endian: le  
seq:    
  - id: header
    type: file_header 
  - id: palette
    type: image_palette
  - id: data
    type: image_indexes     
types:
  file_header:
    seq:
      - id: magic
        contents: '1.22'
      - id: version 
        type: u2
      - id: width 
        type: u2   
      - id: height 
        type: u2   
      - id: palette_size 
        type: u2
  palette_color:
    seq:
      - id: red
        type: u1      
      - id: green
        type: u1       
      - id: blue
        type: u1       
      - id: alpha 
        type: u1       
  image_palette: 
    seq:   
      - id: palette
        type: palette_color
        repeat: expr
        repeat-expr: _root.header.palette_size  
  image_indexes:
    seq:       
      - id: color_index
        type: u1 
        repeat: expr
        repeat-expr: _root.header.width * _root.header.height    