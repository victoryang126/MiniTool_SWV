
#1. 行长度
"""
以下情况除外：
    长的导入模块语句
    注释里的UR
# Python会将 圆括号, 中括号和花括号中的行隐式的连接起来 , 你可以利用这个特点. 如果需要, 你可以在表达式外围增加一对额外的圆括号。


     if (width == 0 and height == 0 and
         color == 'red' and emphasis == 'strong'):
"""

# 2. 空格
"""
按照标准的排版规范来使用标点两边的空格

括号内不要有空格.

按照标准的排版规范来使用标点两边的空格

不要在逗号, 分号, 冒号前面加空格, 但应该在它们后面加(除了在行尾).
Yes: if x == 4:
         print x, y
     x, y = y, x

No:  if x == 4 :
         print x , y
     x , y = y , x

 在二元操作符两边都加上一个空格, 比如赋值(=), 比较(==, <, >, !=, <>, <=, >=, in, not in, is, is not), 布尔(and, or, not). 
 至于算术操作符两边的空格该如何使用, 需要你自己好好判断. 不过两侧务必要保持一致.
 Yes: x == 1
 No:  x<1
 当'='用于指示关键字参数或默认参数值时, 不要在其两侧使用空格.
 Yes: def complex(real, imag=0.0): return magic(r=real, i=imag)
 No:  def complex(real, imag = 0.0): return magic(r = real, i = imag)

"""

# 3. 函数注释

"""
This is a groups style docs.

Args:
  param1 - this is the first param
  param2 - this is a second param

Returns:
    This is a description of what is returned
Raises:
    KeyError - raises an exception
"""

# 4. 类注释

"""Summary of class here.

   Longer class information....
   Longer class information....

   Attributes:
       likes_spam: A boolean indicating if we like SPAM or not.
       eggs: An integer count of the eggs we have laid.
   """

#5. 字符串
"""
避免在循环中用+和+=操作符来累加字符串. 由于字符串是不可变的, 这样做会创建不必要的临时对象, 并且导致二次方而不是线性的运行时间. 
作为替代方案, 你可以将每个子串加入列表, 然后在循环结束后用 .join 连接列表

Yes: items = ['<table>']
     for last_name, first_name in employee_list:
         items.append('<tr><td>%s, %s</td></tr>' % (last_name, first_name))
     items.append('</table>')
     employee_table = ''.join(items)
     
No: employee_table = '<table>'
    for last_name, first_name in employee_list:
        employee_table += '<tr><td>%s, %s</td></tr>' % (last_name, first_name)
    employee_table += '</table>
"""
#6.  命名规则
"""
单字符名称, 除了计数器和迭代器.
包/模块名中的连字符(-)
双下划线开头并结尾的名称(Python保留, 例如__init__)

所谓"内部(Internal)"表示仅模块内可用, 或者, 在类内是保护或私有的.
用单下划线(_)开头表示模块变量或函数是protected的(使用import * from时不会包含).
用双下划线(__)开头的实例变量或方法表示类内私有.
将相关的类和顶级函数放在同一个模块里. 不像Java, 没必要限制一个类一个模块.
对类名使用大写字母开头的单词(如CapWords, 即Pascal风格),
但是模块名应该用小写加下划线的方式(如lower_with_under.py). 
尽管已经有很多现存的模块使用类似于CapWords.py这样的命名, 但现在已经不鼓励这样做, 因为如果模块名碰巧和类名一致, 这会让人困扰.

Type	                                Public	                       Internal
Modules	                                lower_with_under	            _lower_with_under
Packages	                            lower_with_under	 
Classes	                                CapWords	                    _CapWords
Exceptions	                            CapWords	 
Functions	                            lower_with_under()	           _lower_with_under()
Global/Class Constants	                CAPS_WITH_UNDER	                _CAPS_WITH_UNDER
Global/Class Variables	                lower_with_under	            _lower_with_under
Instance Variables	                    lower_with_under	_lower_with_under (protected) or __lower_with_under (private)
Method Names	                        lower_with_under()	_lower_with_under() (protected) or __lower_with_under() (private)
Function/Method Parameters	            lower_with_under	 
Local Variables	                        lower_with_under	 
"""

#7. 代码和导入格式
"""
导入总应该放在文件顶部, 位于模块注释和文档字符串之后, 模块全局变量和常量之前. 导入应该按照从最通用到最不通用的顺序分组:

标准库导入
第三方库导入
应用程序指定导入
每种分组中, 应该根据每个模块的完整包路径按字典序排序, 忽略大小写.

import foo
from foo import bar
from foo.bar import baz
from foo.bar import Quux
from Foob import ar

通常每个语句应该独占一行


"""