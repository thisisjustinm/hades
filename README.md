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
