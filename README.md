[![Azym URL](https://img.shields.io/badge/azym-2ce51-0c0?color=black&labelColor=0c0)](http://azym.ml/?q=2ce51)

![Hades](/hades.png)

Hades is a complex hashing algorithm written in Python.
Hades makes use of the following algorithms to generate a **128-bit hex digest**.


*   Ares (Simple Hashing algorithm)
*   Zeus (Simple Encoding Agoritm)

## Usage

```
from hades import hades

print(hades('string')) 		#for hashing a string
```

## Extra

So far, it is collision resistant, and has pretty fair avalanche effect.


|  ```string```  | ```hash```  |
| --- | ----------- |
| ```I am Hades, a hashing algorithm.``` | ```2ca53472bae9fa0b680d2184965ce042``` |
| ```I am hades, a hashing algorithm.``` | ```f557bf77c1df4649e1ac03f7626b08cd``` |
|  ```I am Hades, a hashing algorithm``` | ```9d3fe1e62c034cdbdafbf8b0358f8f7b``` |
|  ```I am Hades. a hashing algorithm``` | ```64c50e25ad52bc20071cea4181bc39a7``` |
|  ```i am Hades, a hashing algorithm``` | ```9eff43c45d63f1ca3925b2e4c18f6afe``` |
|  ```I am Hades,a hashing algorithm.``` | ```74aeb725355fccad4f8154f147d41cf1``` |
|  ```I'm Hades, a hashing algorithm```  | ```6415c4512427cca312afe784e73883c0``` |
|  ```I am Iades, a hashing algorithm``` | ```a6534aafb71acfa3230adc18d584bd1c``` |



