#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - prints the info of python file
 *
 * @p: PyObject pointer
 * Returns nothing
 */
void print_python_list_info(PyObject *p)
{
	long int weight = PyList_Size(p);
	int val;
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", weight);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (val = 0; val < weight; val++)
		printf("Element %i: %s\n", val, Py_TYPE(obj->ob_item[i])->tp_name);
}
