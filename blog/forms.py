# -*- coding:utf-8 -*-
# Author:Gehao
from django import forms
class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to  = forms.EmailField()
    #comments字段的required=False表示该字段可以没有任何值
    comments = forms.CharField(required=False,widget=forms.Textarea)#使用了widget=forms.Textarea令该字段被渲染为一个<textarea>元素，而不是默认的<input>元素
