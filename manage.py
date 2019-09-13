"""
Copyright (C) 2019 Centro de Computacao Cientifica e Software Livre
Departamento de Informatica - Universidade Federal do Parana - C3SL/UFPR

This file is part of lde-api-regression-test.

lde-api-regression-test is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

lde-api-regression-test is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with lde-api-regression-test.  If not, see <https://www.gnu.org/licenses/>.

"""
from manager import Manager

from regression_test import RegressionTest

manager = Manager()

@manager.command
def save(route=''):
    '''Save multiple or one CSV route'''
    rt = RegressionTest(route)
    rt.save()

@manager.command
def compare(route=''):
    '''Compare multiple or one CSV route'''
    rt = RegressionTest(route)
    rt.compare()


if __name__ == "__main__":
	manager.main()
