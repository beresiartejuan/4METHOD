#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import choice
capchat = """
xD��&������U5����X
&�h[`��ڧ��Ie]�1�M
��bU�!���l��8G|�ohpy����]'n��|bM�� �����/接�=�bN���l�n�Xk����6w�wA����W�GN$�<�
��[�Y1F�� >>(7�h�&=��>��b������j�+��/%�Ќ'�(�Yj������^/s^_��`tz���y�j�(�
X�.���M�)�K�l�@|�0'J�����ip���g�4{����@	�6B�)��a�/�OJpLVm�޽l!�Z�-�珁��j���h�q6͕����)��1E1�S��u����E����y�XN����J�!N"o�̂B�;ﯨb�oCd��O�'��5��O�F:�~ 4�=媃�� Ҝ��!*"cHz0O{�7�J1�6��0M�/2m���.�U��B��%�}`�i*o���ŧ���8�)��VNu�n�S�oڛj��*�)���!�fcp�Q��سX��W��K5�����}���Se���W���[�$qMi+yXm��>e�#��Y%u̖�Wߦ��Q>X+��O;/\��bTx%
>�X�����s <0x1e> ��W�򎂮��jR�K
�u%��4�S�1�`�A��B�F���#אY�I�|o��Ձ�XNw�Q�cn�YG��Q�,��C�ЄP�qǛl��9����7֔b�NC��dK6d���RAH�.>��*�6_�s��������E�����-A�3kS<˓�o��Q�0���T���+K��ƻ��ѯ�-¸Ə�;Y���1�V���ZW���{�n٩���Nٽ�.ze��Q����jsEF�fXiXs^ˤ�F,b������-�eD�lY_�����B�0��n�8!>*r�{�e�PK�T�  �  PK  ��M               manifest.rdf͓�n�0��<�e��@/r(ʹj��5�X/��޾��VQ�������F3ߎ���aȋ���T4c)%�Hh��+:�.���:�ض+��j���*�wn*9_��-7lϳ�(x��<O�"��8qHƴ�	�Bi��|9��	fWQt렐y� =��:���
a�R��� ��@�	Lʄt��NK�3��Q9�����`�Ӄ�<`�+���ވ��^཰���|�hz�czu����#�`�2�O��;y���.��⯴vDl@Σg�����UG�PK��h�  �  PK  ��M               settings.xml�Z[w�8~�_��{
"""
archivo = raw_input("Ingresa la ruta del archivo: ")
ciclos = int(raw_input("Cuantas veces quiere que se sobreescriba?: "))
contador = 1

while contador <= ciclos:
	p = capchat.join([choice(capchat) for i in range(20)])
	f = open(archivo, 'w')
	f.write(str(capchat + p))
	f.close()
	contador += 1

print "---- El archivo no se puede volver a recuperar ----"
