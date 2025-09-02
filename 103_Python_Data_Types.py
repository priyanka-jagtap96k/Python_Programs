"""
Built-in Data Types - 
Text Type    :	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type  :	dict
Set Types  :	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type  :	NoneType"""

x = 'You are good person'
print(f"Text Type str Example : {x}")

x = 10
y = 10.10
z = 1j
print(f"Numeric Types:	int, float, complex : {x},{y},{z}")

x = [10,20,30]
y = ('piuu','vivek','arsh')
z = range(3)
print(f"Sequence Types:	list, tuple, range : {x},{y},{z}")

x = {"name":"piuu","age":21}
print(f"Mapping Type  :	dict : {x}")

x = {10,20,30}
y = frozenset({10,20,30})
print(f"Set Types  : set, frozenset : {x}, {y}")

x = False
print(f"Boolean Type : bool :{x}")

x = b"hello"
y = bytearray(5)
z = memoryview(bytes(5))
print(f"Binary Types : bytes, bytearray, memoryview : {x},{y},{z}")

x = None
print(f"None Type  : NoneType : {x}")