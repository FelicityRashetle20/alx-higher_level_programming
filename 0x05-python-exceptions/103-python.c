#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Prints a maximum of 10 bytes
 * @p: Python Byte Object
 * If p is not valid, print error message
 */
void print_python_bytes(PyObject *p)
{
	char *byte_word;
	long int weight, i, bound;

	setbuf(stdout, NULL);

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		setbuf(stdout, NULL);
		return;
	}

	weight = ((PyVarObject *)(p))->ob_size;
	byte_word = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", weight);
	printf("  trying string: %s\n", byte_word);

	if (weight >= 10)
		bound = 10;
	else
		bound = weight + 1;

	printf("  first %ld bytes:", bound);

	for (i = 0; i < bound; i++)
		if (byte_word[i] >= 0)
			printf(" %02x", byte_word[i]);
		else
			printf(" %02x", 256 + byte_word[i]);

	printf("\n");
	setbuf(stdout, NULL);
}

/**
 * print_python_list - Prints information of list
 * @p: Python Byte Object
 * ip @p not valid, print error message
 */
void print_python_list(PyObject *p)
{
	long int weight, i;
	PyListObject *point_list;
	PyObject *obj_pointer;

	setbuf(stdout, NULL);
	printf("[*] Python list info\n");

	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		setbuf(stdout, NULL);
		return;
	}

	weight = ((PyVarObject *)(p))->ob_size;
	point_list = (PyListObject *)p;

	printf("[*] Size of the Python List = %ld\n", weight);
	printf("[*] Allocated = %ld\n", point_list->allocated);

	for (i = 0; i < weight; i++)
	{
		obj_pointer = point_list->ob_item[i];
		printf("Element %ld: %s\n", i, ((obj_pointer)->ob_type)->tp_name);

		if (PyBytes_Check(obj_pointer))
			print_python_bytes(obj_pointer);
		if (PyFloat_Check(obj_pointer))
			print_python_float(obj_pointer);
	}
	setbuf(stdout, NULL);
}

/**
 * print_python_float - Prints information of float
 * @p: Python Byte Object
 * If @p not valid, print error message
 */
void print_python_float(PyObject *p)
{
	double value;
	char *new_pointer;

	setbuf(stdout, NULL);
	printf("[.] float object info\n");

	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		setbuf(stdout, NULL);
		return;
	}

	value = ((PyFloatObject *)(p))->ob_fval;
	new_pointer = PyOS_double_to_string(value, 'r', 0, Py_DTSF_ADD_DOT_0, Py_DTST_FINITE);

	printf("  value: %s\n", new_pointer);
	setbuf(stdout, NULL);
}

