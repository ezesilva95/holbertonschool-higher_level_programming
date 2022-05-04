#include <Python.h>
#include <listobject.h>
#include <object.h>
#include <stdio.h>

/**
 * print_python_list_info - prints some basic info about Python lists.
 * @p: = pointer to PyObject
 **/
void print_python_list_info(PyObject *p)
{
	int size = PyList_Size(p);
	int alloc = ((PyListObject *)p)->allocated;
	int i = 0;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);
	for (i = 0; i < size; i++)
	{
		printf("Element %ld: %s\n",
		       idx,
		       (PY_TYPE(PyList_GetItem(p, i)))->tp_name);
	}
}
