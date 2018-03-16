### MiaoDump
喵dump是一个用于dump iOS头文件的工具，可以生成用于预编译的替换字符串的头文件(~~混淆~~)，你可以把他当做ppios-rename或者ios-class-guard
，或者念茜build-script的混淆方法，miaodump使用起来会更加方便。


### Require
None


### Installation
```sudo python setup.py install```

### Usage
1. Normal
```
miaodump -p /path/to/inputdir -o /path/to/outputdir
```
2. Exclude external libraries
```
miaodump -p /path/to/inputdir -e="AFNetworking,CoreModel" -o /path/to/outputdir
```
Filtering sdk using built-in lists
```
miaodump -p /path/to/inputdir -e="AFNetworking,CoreModel" -o /path/to/outputdir -ed
```
3. Using binary 
```
miaodump -p /path/to/inputdir -e="AFNetworking,CoreModel" -o /path/to/outputdir -ed --arch
```
`--arch` using binary (class-dump)


### Doc



### Author
ch4r0n(xingrenchan@gmail.com)


### Changelog 
* v0.0.1  
最基本的功能