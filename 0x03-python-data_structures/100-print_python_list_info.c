#include <Python.h>
#include <listobject.h>
#include <object.h>
#include <stdio.h>

void print_python_list_info(PyObject *p)
{
	int idx;
	int alloc = ((PyListObject *)p)->allocated;
	size_t size = PyList_Size(p);

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);
	for (idx = 0; idx < size; idx++)
	{
		printf("Element %ld: %s\n",
		       idx,
		       (PY_TYPE(PyList_GetItem(p, idx)))->tp_name);
	}
}
