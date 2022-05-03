#include <Python.h>

void print_python_list_info(PyObject *p)
{
	idx = 0;
	int size = PyList_Size(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", alloc);
	for (idx = 0; idx < size; idx++)
		printf("Element %li: %s\n", idx,
			(PY_TYPE(PyList_GetItem(p, idx)))->tp_name);
}

