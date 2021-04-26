#coding=utf-8
from __future__ import unicode_literals 

import streamlit as st
import streamlit.components.v1 as components
from streamlit_folium import folium_static

# EDA pkgs
import  pandas as pd
import seaborn as sns
import folium as fl
import pydeck as pdk
from pyecharts.charts import Pie, Bar, Polar, TreeMap,Funnel, Tree, Timeline
from pyecharts.commons.utils import JsCode
from pyecharts.components import Table
from pyecharts.options import ComponentTitleOpts
from pyecharts import options as opts
from pyecharts.faker import Faker
from streamlit_echarts import st_pyecharts




#Data Viz
import matplotlib.pyplot as plt 
import matplotlib


def getData():
    data = st.file_uploader('Upload Dataset', type=['csv', 'txt'])
    return data

def pieChart(df):
    def randomcolor(kind):
        colors =[]
        for i in range(kind):
            #colArr = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F','G','H','I','K','L','M','N']
            colArr = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
            color  =''
            for i in range(6):
                color += colArr[random.randint(0,14)]
                colors.append('#' + color)
        return colors
            

   
    all_columns = df.columns
    type_of_plot = st.selectbox("Select Type of Plot",["PIE1","PIE2","PIE3"])
    columns_to_plot = st.selectbox("Select 1 column",all_columns,key='a' )
    columns_to_plot1 = st.selectbox("Select 1 column",all_columns, key='b' )
    
    if st.button("Generate Plot"):
        
        #st.success("Generating Customizable Plot of {} for {}".format(type_of_plot))
        
        if type_of_plot == 'PIE1':
           
            cje = df[columns_to_plot].tolist()
            other_var = df[columns_to_plot1].tolist()
            color_series = randomcolor(len(cje))
            pie = Pie()
            pie.add('', [list(z) for z in zip(cje, other_var)],
            radius=['30%', '135%'],
            center=['50%', '65%'],
             rosetype='area')
            
            pie.set_global_opts(title_opts =opts.TitleOpts(title='Population Generale des 20 CJE de Montreal'),
                                legend_opts=opts.LegendOpts(is_show=False), toolbox_opts=opts.ToolboxOpts())
            pie.set_series_opts(label_opts=opts.LabelOpts(is_show=True, position='inside', font_size=12,
    formatter='{b}:{c}',font_style='italic', font_weight='bold', font_family='Microsoft YaHei'))
            pie.set_colors(color_series)
            return pie
            
    #     if type_of_plot == 'PIE2':
    #         cje = df[columns_to_plot].tolist()
    #         other_var = df[columns_to_plot1].tolist()
    #         color_series = randomcolor(len(cje))
    #         pie = Pie()
    #         pie.add('', [list(z) for z in zip(cje, other_var)], radius=["40%","75%"])
            
    #         pie.set_global_opts(title_opts =opts.TitleOpts(title='Population Generale des 20 CJE de Montreal'),
    #                             legend_opts=opts.LegendOpts(orient='horizontal',pos_bottom='-3%',pos_left="2%"), toolbox_opts=opts.ToolboxOpts())
    #         pie.set_series_opts(label_opts=opts.LabelOpts(is_show=True, position='inside', font_size=12,
    # formatter='{b}:{c}',font_style='italic', font_weight='bold', font_family='Microsoft YaHei'))
    #         pie.set_colors(color_series)
    #         return pie
    #     if type_of_plot == 'PIE3':
    #         cje = df[columns_to_plot].tolist()
    #         other_var = df[columns_to_plot1].tolist()
    #         color_series = randomcolor(len(cje))
    #         pie = Pie()
    #         pie.add('', [list(z) for z in zip(cje, other_var)], radius=["40%","75%"],rosetype="area")
            
    #         pie.set_global_opts(title_opts =opts.TitleOpts(title='Population Generale des 20 CJE de Montreal'),
    #                             legend_opts=opts.LegendOpts(orient='horizontal',pos_bottom='-3%',pos_left="2%"), toolbox_opts=opts.ToolboxOpts())
    #         pie.set_series_opts(label_opts=opts.LabelOpts(is_show=True, position='inside', font_size=12,
    # formatter='{b}:{c} ',font_style='italic', font_weight='bold', font_family='Microsoft YaHei'))
    #         pie.set_colors(color_series)
            
    #         return pie
 
def barChart(df):
    type_of_plot = st.selectbox("Select Type of Plot",["BAR1","BAR2","BAR3","BAR4","BAR5"])
    all_columns = df.columns
    
        
        #st.success("Generating Customizable Plot of {} for {}".format(type_of_plot))
        
    if type_of_plot == 'BAR1':
        columns_to_plot = st.selectbox("Select 1 column",all_columns,key='a' )
        columns_to_plot1 = st.selectbox("Select 2 column",all_columns, key='b' )
        columns_to_plot2 = st.selectbox("Select 3 column",all_columns, key='c' )
    
        cje = df[columns_to_plot].tolist()
        other_var = df[columns_to_plot1].tolist()
        other_var1 = df[columns_to_plot2].tolist()
        bar = Bar(init_opts = opts.InitOpts(width='900px', height='1200px'))
        bar.add_xaxis(cje)
        bar.add_yaxis(columns_to_plot1, other_var)
        bar.add_yaxis(columns_to_plot2, other_var1)
        bar.set_global_opts(toolbox_opts=opts.ToolboxOpts())
        bar.reversal_axis()
        bar.set_series_opts(label_opts=opts.LabelOpts(position="right"), markline_opts=opts.MarkLineOpts(
            data=[
                opts.MarkLineItem(type_="min", name="最小值"),
                opts.MarkLineItem(type_="max", name="最大值"),
                opts.MarkLineItem(type_="average", name="平均值"),
            ]
        ),)
            #bar.set_global_opts(title_opts=opts.TitleOpts(title="Bar-Test Rendered Pictures"))
        # st.button("Generate Plot")
        return bar
        
    if type_of_plot == 'BAR2':
        
        columns_to_plot = st.selectbox("Select 1 column",all_columns,key='a' )
        columns_to_plot1 = st.selectbox("Select 2 column",all_columns, key='b' )
        cje = df[columns_to_plot].tolist()
        other_var = df[columns_to_plot1].tolist()
        bar = Bar(init_opts = opts.InitOpts(width='900px', height='1800px'))
        bar.add_xaxis(cje)
        bar.add_yaxis(columns_to_plot1, other_var, gap="0%")
       
        bar.set_global_opts(toolbox_opts=opts.ToolboxOpts(), 
                             xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=65)), 
                             brush_opts=opts.BrushOpts()
        )
            
        bar.set_series_opts(
     
        markline_opts=opts.MarkLineOpts(
            data=[
                opts.MarkLineItem(type_="min", name="最小值"),
                opts.MarkLineItem(type_="max", name="最大值"),
                opts.MarkLineItem(type_="average", name="平均值"),
            ]
        ),
    )
        return bar
    
    if type_of_plot == 'BAR3':
        columns_to_plot = st.selectbox("Select 1 column",all_columns,key='a' )
        columns_to_plot1 = st.selectbox("Select 2 column",all_columns, key='b' )
        columns_to_plot2 = st.selectbox("Select 3 column",all_columns, key='c' )
        columns_to_plot3 = st.selectbox("Select 4 column",all_columns, key='d' )
        columns_to_plot4 = st.selectbox("Select 5 column",all_columns, key='e' )
        cje = df[columns_to_plot].tolist()
        other_var1 = df[columns_to_plot1].tolist()
        other_var2 = df[columns_to_plot2].tolist()
        other_var3 = df[columns_to_plot3].tolist()
        other_var4 = df[columns_to_plot4].tolist()
        bar = Bar(init_opts = opts.InitOpts(width='900px', height='1200px'))
        bar.add_xaxis(cje)
        bar.add_yaxis(columns_to_plot1, other_var1)
        bar.add_yaxis(columns_to_plot2, other_var2)
        bar.add_yaxis(columns_to_plot3, other_var3)
        bar.add_yaxis(columns_to_plot4, other_var4)
      
        bar.reversal_axis()
        #bar.add_yaxis(columns_to_plot1, other_var, gap="0%")
       
        bar.set_global_opts(toolbox_opts=opts.ToolboxOpts(), 
                             xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=65)), 
                             brush_opts=opts.BrushOpts()
        )
        grid = Grid()
        grid.add(bar, grid_bottom="60%")
        return bar

def funnelChart(df):
    all_columns = df.columns
    columns_to_plot = st.selectbox("Select 1 column",all_columns,key='aa' )
    columns_to_plot1 = st.selectbox("Select 2 column",[col for col in df.columns if col not in [columns_to_plot]], key='bb' )
        # columns_to_plot2 = st.selectbox("Select 1 column",all_columns, key='c' )
        # columns_to_plot3 = st.selectbox("Select 1 column",all_columns, key='d' )
        # columns_to_plot4 = st.selectbox("Select 1 column",all_columns, key='e' )
    cje = df[columns_to_plot].tolist()
    other_var1 = df[columns_to_plot1].tolist()
        # other_var2 = df[columns_to_plot2].tolist()
        # other_var3 = df[columns_to_plot3].tolist()
        # other_var4 = df[columns_to_plot4].tolist()
        
        
    funnel = Funnel(init_opts = opts.InitOpts(width='900px', height='1200px'))
    funnel.add('', [list(z) for z in zip(cje, other_var1)],
        label_opts=opts.LabelOpts(position="inside"),)
        
        
       
    return funnel
        
def polarChart(df):
     type_of_plot = st.selectbox("Select Type of Plot",["POLAR1","POLAR2","POLAR3 Angle"])
     all_columns = df.columns
    
        
        #st.success("Generating Customizable Plot of {} for {}".format(type_of_plot))
        
     if type_of_plot == 'POLAR1':
           
            columns_to_plot = st.selectbox("Select 1 column",all_columns,key='a' )
            
            columns_to_plot1 = st.selectbox("Select 1 column",[col for col in df.columns if col not in [columns_to_plot]], key='b' )
        # columns_to_plot2 = st.selectbox("Select 1 column",all_columns, key='c' )
            n = df[[columns_to_plot, columns_to_plot1]].sort_values(by = columns_to_plot1 , ascending = True)
            cje = n[columns_to_plot].tolist()
            other_var = n[columns_to_plot1].tolist()
          
           
            # cje = df[columns_to_plot].tolist()
            # other_var = df[columns_to_plot1].sort_values(ascending = True).tolist()
        # other_var1 = df[columns_to_plot2].tolist()
            polar = Polar()
            polar.add_schema( 
       radiusaxis_opts=opts.RadiusAxisOpts( data = cje ,type_="category",
                                                splitline_opts=opts.SplitLineOpts(is_show=False),
                                                axisline_opts=opts.AxisLineOpts(is_show=False),
                                                axistick_opts=opts.AxisTickOpts(is_show=False)),
            angleaxis_opts=opts.AngleAxisOpts(is_clockwise=True,
                                              splitline_opts=opts.SplitLineOpts(is_show=False),
                                              axisline_opts=opts.AxisLineOpts(is_show=False),
                                              axislabel_opts=opts.LabelOpts(is_show=False),
                                              axistick_opts=opts.AxisTickOpts(is_show=False)))
            polar.add(columns_to_plot1, other_var, type_="bar")
            polar.set_global_opts(toolbox_opts=opts.ToolboxOpts())
            polar.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
       
            return polar
        
        
        
     if type_of_plot == 'POLAR2':
            columns_to_plot = st.selectbox("Select 1 column",all_columns,key='a' )
            columns_to_plot1 = st.selectbox("Select 1 column",[col for col in df.columns if col not in [columns_to_plot]], key='b' )
            columns_to_plot2 = st.selectbox("Select 1 column",[col for col in df.columns if col not in [columns_to_plot1, columns_to_plot]], key='c' )
            columns_to_plot3 = st.selectbox("Select 1 column",[col for col in df.columns if col not in [columns_to_plot1, columns_to_plot2,columns_to_plot]], key='c' )
            columns_to_plot4 = st.selectbox("Select 1 column",[col for col in df.columns if col not in [columns_to_plot1, columns_to_plot2,columns_to_plot, columns_to_plot3]], key='c' )
            n = df[[columns_to_plot, columns_to_plot1, columns_to_plot2, columns_to_plot3, columns_to_plot4]].sort_values(by = columns_to_plot1 , ascending = True)
            
            cje = n[columns_to_plot].tolist()
            other_var = n[columns_to_plot1].tolist()
            other_var2 = n[columns_to_plot2].tolist()
            other_var3 = n[columns_to_plot3].tolist()
            other_var4 = n[columns_to_plot4].tolist()
          

            polar = Polar()
            polar.add_schema( 
       radiusaxis_opts=opts.RadiusAxisOpts( data = cje ,type_= "category",
                                                splitline_opts=opts.SplitLineOpts(is_show=False),
                                                axisline_opts=opts.AxisLineOpts(is_show=False),
                                                axistick_opts=opts.AxisTickOpts(is_show=False)),
            angleaxis_opts=opts.AngleAxisOpts(is_clockwise=True,
                                              splitline_opts=opts.SplitLineOpts(is_show=False),
                                              axisline_opts=opts.AxisLineOpts(is_show=False),
                                              axislabel_opts=opts.LabelOpts(is_show=False),
                                              axistick_opts=opts.AxisTickOpts(is_show=False)))
            polar.add(columns_to_plot1, other_var, type_="bar" )
            polar.add(columns_to_plot2, other_var2, type_="bar")
            polar.add(columns_to_plot3, other_var3, type_="bar")
            polar.add(columns_to_plot4, other_var4, type_="bar")
            polar.set_global_opts(toolbox_opts=opts.ToolboxOpts())
            polar.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
       
            return polar
        
     if type_of_plot == 'POLAR3 Angle':
            columns_to_plot = st.selectbox("Select 1 column",all_columns,key='a' )
            columns_to_plot1 = st.selectbox("Select 1 column",[col for col in df.columns if col not in [columns_to_plot]], key='b' )
            columns_to_plot2 = st.selectbox("Select 1 column",[col for col in df.columns if col not in [columns_to_plot1, columns_to_plot]], key='c' )
            columns_to_plot3 = st.selectbox("Select 1 column",[col for col in df.columns if col not in [columns_to_plot1, columns_to_plot2,columns_to_plot]], key='c' )
            columns_to_plot4 = st.selectbox("Select 1 column",[col for col in df.columns if col not in [columns_to_plot1, columns_to_plot2,columns_to_plot, columns_to_plot3]], key='c' )
            n = df[[columns_to_plot, columns_to_plot1, columns_to_plot2, columns_to_plot3, columns_to_plot4]].sort_values(by = columns_to_plot1 , ascending = True)
            
            cje = n[columns_to_plot].tolist()
            other_var = n[columns_to_plot1].tolist()
            other_var2 = n[columns_to_plot2].tolist()
            other_var3 = n[columns_to_plot3].tolist()
            other_var4 = n[columns_to_plot4].tolist()
          

            polar = Polar()
            polar.add_schema( 
    #    radiusaxis_opts=opts.RadiusAxisOpts( data = cje ,type_= "category",
    #                                             splitline_opts=opts.SplitLineOpts(is_show=False),
    #                                             axisline_opts=opts.AxisLineOpts(is_show=False),
    #                                             axistick_opts=opts.AxisTickOpts(is_show=False)),
            angleaxis_opts=opts.AngleAxisOpts(is_clockwise=True,type_= "category",
                                              splitline_opts=opts.SplitLineOpts(is_show=False),
                                              axisline_opts=opts.AxisLineOpts(is_show=False),
                                              axislabel_opts=opts.LabelOpts(is_show=False),
                                              axistick_opts=opts.AxisTickOpts(is_show=False)))
            polar.add(columns_to_plot1, other_var, type_="bar", stack="stack0" )
            polar.add(columns_to_plot2, other_var2, type_="bar" , stack="stack0")
            polar.add(columns_to_plot3, other_var3, type_="bar" , stack="stack0")
            polar.add(columns_to_plot4, other_var4, type_="bar" , stack="stack0")
            polar.set_global_opts(toolbox_opts=opts.ToolboxOpts())
            polar.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
       
            return polar
    
def mapChart(df):
    type_of_plot = st.selectbox("Select Type of Plot",["Map1","Map2","Map3"])
    all_columns = df.columns
    if type_of_plot == 'Map1':
        columns_to_plot = st.selectbox("Select 1 column",all_columns,key='a' )      
        columns_to_plot1 = st.selectbox("Select 2 lng",[col for col in df.columns if col not in [columns_to_plot]], key='b' )
        columns_to_plot2 = st.selectbox("Select 3 lat",[col for col in df.columns if col not in [columns_to_plot, columns_to_plot1]], key='c' )
        # columns_to_plot3 = st.selectbox("Select 3 Value",[col for col in df.columns if col not in [columns_to_plot, columns_to_plot1, columns_to_plot2]], key='d' )
        # df[columns_to_plot1] = pd.to_numeric(df[columns_to_plot1])
        # df[columns_to_plot2] = pd.to_numeric(df[columns_to_plot2])
        ele = df[columns_to_plot]
        midpoint = (np.average( df[columns_to_plot1]), np.average( df[columns_to_plot2]))
        midpoint
        layer = pdk.Layer(
            "HexagonLayer",
            data=df[[columns_to_plot1, columns_to_plot2]],
            get_position=[columns_to_plot1, columns_to_plot2],
            auto_highlight = True,
            get_elevation = [columns_to_plot],
        radius = 1000,
        extruded = True,
        pickable = True,
        elevation_scale = 5000,
        elevation_range =[0, 20000],    
)
        # Set the viewport location
        view_state = pdk.ViewState(
                midpoint[0],  midpoint[1], zoom=11,  pitch=50
        )

        # Combined all of it and render a viewport
        r = pdk.Deck(
            map_style="mapbox://styles/mapbox/light-v9",
            layers=[layer],
            initial_view_state=view_state,
            tooltip={"html": "<b>Elevation Value:</b>{elevationValue} ", "style": {"color": "white"}},
        )
        return r
        
    if type_of_plot == 'Map2':
        columns_to_plot = st.selectbox("Select 1 column",all_columns,key='a' )      
        columns_to_plot1 = st.selectbox("Select 2 lng",[col for col in df.columns if col not in [columns_to_plot]], key='b' )
        columns_to_plot2 = st.selectbox("Select 3 lat",[col for col in df.columns if col not in [columns_to_plot, columns_to_plot1]], key='c' )
        
        st.map(df)
        
    if type_of_plot == 'Map3':
        columns_to_plot = st.selectbox("Select 1 column",all_columns,key='a' )      
        columns_to_plot1 = st.selectbox("Select 2 lng",[col for col in df.columns if col not in [columns_to_plot]], key='b' )
        columns_to_plot2 = st.selectbox("Select 3 lat",[col for col in df.columns if col not in [columns_to_plot, columns_to_plot1]], key='c' )
        columns_to_plot3 = st.selectbox("Select 3 Value",[col for col in df.columns if col not in [columns_to_plot, columns_to_plot1, columns_to_plot2]], key='d' )
        df[columns_to_plot1] = pd.to_numeric(df[columns_to_plot1])
        df[columns_to_plot2] = pd.to_numeric(df[columns_to_plot2])
        ele = df[columns_to_plot]
   
        midpoint = (np.average( df[columns_to_plot1]), np.average( df[columns_to_plot2]))
        m = fl.Map(location=[df[columns_to_plot1][0], df[columns_to_plot2][0]], zoom_start=16)
        for lat, lng, value,label in zip(df[columns_to_plot1], df[columns_to_plot2], df[columns_to_plot], df[columns_to_plot3]):
            fl.Marker(
        [lat, lng],
        radius=5, # define how big you want the circle markers to be
        color='yellow',
        fill=True,
        popup = [label, value],
        fill_color='blue',
        fill_opacity=0.6
            ).add_to(m)

        return folium_static(m)
    
def treeChart(df):
    tree = Tree()
    tree.add('',  df, 
        orient="TB",
        label_opts=opts.LabelOpts(
            position="top",
            horizontal_align="right",
            vertical_align="middle",
            rotate=-90,
        ),
    )
    tree.set_global_opts(title_opts=opts.TitleOpts(title="Tree"))
    return tree
       

def treeMapChart(df):
    
    type_of_plot = st.selectbox("Select Type of Plot",["TreeMap1 Multi-level","TreeMap2"])
    #  allc = list(df.columns[:20])
    #  allc
    #  tmap = px.treemap(df,path=[allc, "Enfants de 0 à 14 ans", "CJE"], values= "Population 2016")
    #  return tmap
    all_columns = df.columns
    treemap = TreeMap()
  
    if type_of_plot == "TreeMap1 Multi-level":
        columns_to_plot = st.selectbox("Select 1 column",all_columns,key='a' )
        columns_to_plot1 = st.selectbox("Select 2 column",[col for col in df.columns if col not in [columns_to_plot]], key='b' )
        # columns_to_plot2 = st.selectbox("Select 3 column",[col for col in df.columns if col not in [columns_to_plot, columns_to_plot1]], key='c' )
           
        names = list(df[columns_to_plot])
        
        def get_all_values(d):
            if isinstance(d, dict):
                for v in d.values():
                    yield from get_all_values(v)
            elif isinstance(d, list):
                for v in d:
                    yield from get_all_values(v)
            else:
                yield d 
        dictionaryObject = df.to_dict();
        # print(list(get_all_values(dictionaryObject)))       
        df2 = df.copy()
        df3 = df.drop('CJE', axis=1)

        df3.values.tolist()
        values_market = df3.values.tolist()
        df2 = df.copy()
        # print(values_market)   
        childs = []
        for j,indu_one in enumerate(names):
               data_now = df2[df2[columns_to_plot]==indu_one]
               data_1 = list(data_now[columns_to_plot])
            #    print(data_now.values.tolist())
               
               child = []
               child.extend({'name':data_1[i],'value':list(data_now[columns_to_plot])[i]} for i in range(0,len(data_now[columns_to_plot])))
               childs.append(child)

        data_n = [{ 'name':i,'value':j, 'children': m} for i,j,m in zip(names,values_market,childs)]
     
        treemap.add(series_name="option",data=data_n,visual_min=300,leaf_depth=1,
       
        label_opts=opts.LabelOpts(position="inside"),)
       
        return treemap
 
 
 
    if type_of_plot == "TreeMap2":
        
            columns_to_plot = st.selectbox("Select 1 column",all_columns,key='a' )
            columns_to_plot1 = st.selectbox("Select 1 column",[col for col in df.columns if col not in [columns_to_plot]], key='b' )
    
            names = list(df[columns_to_plot])

            values_market = list(df[columns_to_plot1])

            df2 = df.copy()
            childs = []

            data_n = [{'name':i, 'value':j,'value1':j} for i,j in zip(names,values_market)]
   
           


       
        # treemap = TreeMap(init_opts=opts.InitOpts(height='1080px',width='1920px'))
            treemap.add(
        series_name=columns_to_plot1,
        data=data_n,
        leaf_depth=2,
        node_click="zoomToNode",  
        zoom_to_node_ratio=0.5*0.5,
    
        levels=[
            opts.TreeMapLevelsOpts(
                #color_mapping_by='value',
                     upper_label_opts= opts.LabelOpts(position="inside") ,     
                treemap_itemstyle_opts=opts.TreeMapItemStyleOpts(
                    border_color="#555", border_width=4, gap_width=4
                )
            ),
            opts.TreeMapLevelsOpts(
                 upper_label_opts= opts.LabelOpts(position="inside"), 
                color_saturation=[0.3, 0.6],
                treemap_itemstyle_opts=opts.TreeMapItemStyleOpts(
                    border_color_saturation=0.7, gap_width=2, border_width=2
                ),
            ),
            # opts.TreeMapLevelsOpts(
               
            #     color_saturation=[0.3, 0.5],
            #     treemap_itemstyle_opts=opts.TreeMapItemStyleOpts(
            #         border_color_saturation=0.6, gap_width=1
            #     ),
            # ),
            # opts.TreeMapLevelsOpts(color_saturation=[0.3, 0.5]),
        ],
    )
            treemap.set_series_opts(label_opts=opts.LabelOpts(
        is_show = True,
        position = 'inside',# position  'top'，'left'，'right'，'bottom'，'inside'，'insideLeft'，'insideRight'.....
        font_size = 20,
        # color 
        color= '#ffffff',
    
        # font_style 'normal'，'italic'，'oblique'
        font_style = 'nomal' , 
            
        # font_weight  'normal'，'bold'，'bolder'，'lighter'
        font_weight = None,
            
        # font_family  'Arial', 'Courier New', 'Microsoft YaHei' ....
        font_family = 'Microsoft YaHei',
            
        # rotate  -90 90 
        rotate = '0',
            
        # margin 
        margin = 20,
            
        interval = None,
            
        # horizontal_align 'left'，'center'，'right'
        horizontal_align = 'center',
            
        # vertical_align ：'top'，'middle'，'bottom'
        vertical_align = None,
      ) )
            treemap.set_global_opts(toolbox_opts=opts.ToolboxOpts(pos_left='8%'), 
        title_opts=opts.TitleOpts(title="TreeMap")) 
    return treemap 

def timelineChart(df):
    x = Faker.choose()
    tl = Timeline()
    for i in range(2015, 2020):
        bar = (
            Bar()
            .add_xaxis(x)
            .add_yaxis("商家A", Faker.values())
            .add_yaxis("商家B", Faker.values())
            .set_global_opts(
                title_opts=opts.TitleOpts("某商店{}年营业额 - With Graphic 组件".format(i)),
                toolbox_opts=opts.ToolboxOpts(), brush_opts=opts.BrushOpts(),
                graphic_opts=[
                    opts.GraphicGroup(
                        graphic_item=opts.GraphicItem(
                            rotation=JsCode("Math.PI / 4"),
                            bounding="raw",
                            right=100,
                            bottom=110,
                            z=100,
                        ),
                        children=[
                            opts.GraphicRect(
                                graphic_item=opts.GraphicItem(
                                    left="center", top="center", z=100
                                ),
                                graphic_shape_opts=opts.GraphicShapeOpts(
                                    width=400, height=50
                                ),
                                graphic_basicstyle_opts=opts.GraphicBasicStyleOpts(
                                    fill="rgba(0,0,0,0.3)"
                                ),
                            ),
                            opts.GraphicText(
                                graphic_item=opts.GraphicItem(
                                    left="center", top="center", z=100
                                ),
                                graphic_textstyle_opts=opts.GraphicTextStyleOpts(
                                    text="某商店{}年营业额".format(i),
                                    font="bold 26px Microsoft YaHei",
                                    graphic_basicstyle_opts=opts.GraphicBasicStyleOpts(
                                        fill="#fff"
                                    ),
                                ),
                            ),
                        ],
                    )
                ],
            )
        )
        tl.add(bar, "{}年".format(i)) 
        return tl  
    
        
def main():
    
    html_temp = """
		<div style="background-color:#45637d;padding:10px;border-radius:10px">
		<h1 style="color:white;text-align:center;">A-DAConsultancy</h1>
        <h4 style="color:white;text-align:center;text-decoration: underline">Semi Auto Machine Learning App</h4>
        <em style="color:white;text-align:center; margin-top:33px ">Using Streamlit = 0.78.0+</em>  
		</div>
		"""
    components.html(html_temp, height=300)

    # st.subheader('Semi Auto ML App ')
    # st.text('Using Streamlit == 0.78.0+')

    activities =[ 'EDA', 'Plot', 'Model Building', 'Other Projects','About']
    
    choice =  st.sidebar.selectbox('Select Activity', activities)
    if choice == 'EDA':
        st.subheader('Exploratory data analysis')
        data = getData()
        if data is not None:
            df = pd.read_csv(data)
            st.dataframe(df.head())
            
            if st.checkbox('show shape / Data types / Na(s) values'):
                
                col1, col2, col3 = st.beta_columns(3)
                
                col1.success('Shape of dataFrame')
                col1.write(df.shape)
              
                col2.success('Na(s) values')
                col2.write(df.isnull().sum().sum())
                
                col3.success('Data type')
                col3.write(df.dtypes)
                
            if st.checkbox('Show Columns'):
                all_columns = df.columns.tolist()
                st.write(all_columns)
                     
            if st.checkbox('Show Summary'):
                st.write(df.describe())
            
    
            if st.checkbox('Last 5 columns'):
                st.write(df.tail())
        
            if st.checkbox('Pick Columns'):
                selected_columns = st.multiselect('Select Columns', df.columns.tolist())
                new_df = df[selected_columns]
                st.dataframe(new_df) 
                 
            if st.checkbox('Highlight_max'):
                st.dataframe(df.style.highlight_max(axis=0))
            
            if st.checkbox('Transform to table'):
                selected_columns = st.multiselect('Select Columns', df.columns.tolist())
                new_df = df[selected_columns]
                st.table(new_df) 
            
            
    
    elif choice == 'Plot':
        st.subheader('Data visualization')
       
        data = getData()
        if data is not None:
            df = pd.read_csv(data)
            st.dataframe(df.head())
            
        if  st.checkbox('Correlation  with seaborn'):
            if data is not None:
                fig, ax = plt.subplots(figsize=(20,15))
                st.write(sns.heatmap(df.corr(), annot=True))
                st.pyplot(fig) 
            else:
                st.warning('NO DATA')
        
        if  st.checkbox('Pairplot'):
            if data is not None:
                fig, ax = plt.subplots(figsize=(20,15))
                st.write(sns.pairplot(df))
                st.pyplot(fig) 
            else:
                st.warning('NO DATA')
                      
        if  st.checkbox('Pie Chart'):
            if data is not None:
                pie = pieChart(df)        
                st.write(st_pyecharts(pie ,height="800px" ,theme={
                "backgroundColor": "#eeeee4",
                "textStyle": {"color": "#0080ff"},
            }))              
            else:
                st.warning('NO DATA')
        
        if  st.checkbox('Bar Chart'):
            
            if data is not None:
                bar = barChart(df)
         
                st.write(st_pyecharts(bar ,height="900px" ,theme={
                "backgroundColor": "#eeeee4",
                "textStyle": {"color": "#0080ff"},
            },))
            else:
                st.warning('NO DATA')
            
        if  st.checkbox('Polar Chart'):            
            if data is not None:
                polar = polarChart(df)
         
                st.write(st_pyecharts(polar ,height="900px" ,theme={
                "backgroundColor": "#eeeee4",
                "textStyle": {"color": "#0080ff"},
            },))
            else:
                st.warning('NO DATA')
        
        if  st.checkbox('HexagonLayer/ScatterplotLayer/light map'):
            
            if data is not None:
                map = mapChart(df)
                st.write((map ))
            else:
                st.warning('NO DATA')   
                
                 
        if  st.checkbox('TreeMap'):
            
            if data is not None:
               treemap = treeMapChart(df)
               st.write(st_pyecharts(treemap,height='700px',width='1920px' ,theme={
                "backgroundColor": "#eeeee4",
                "font_size":20
            },))
            
            else:
                st.warning('NO DATA') 
        
        if  st.checkbox('Tree'):
            
            if data is not None:
               tree = treeChart(df)
               st.write(st_pyecharts(tree,height='700px',width='1920px' ,theme={
                "backgroundColor": "#eeeee4",
                "font_size":20
            },))
            
            else:
                st.warning('NO DATA')     
         
         
        if  st.checkbox('Funnel'):
            
            if data is not None:
               funnel = funnelChart(df)
               st.write(st_pyecharts(funnel,height='700px',width='1920px' ,theme={
                "backgroundColor": "#eeeee4",
                "font_size":20
            },))
            
            else:
                st.warning('NO DATA')
        
        if  st.checkbox('Timeline_bar_with_graphic'):
                
            if data is not None:
               timeline = timelineChart(df)
               st.write(st_pyecharts(timeline,height='700px',width='1920px' ,theme={
                "backgroundColor": "#eeeee4",
                "font_size":20
            },))
            
            else:
                st.warning('NO DATA')     
        
            
    
    elif choice == 'Model Building':
        st.subheader('Model Building')
        data = st.file_uploader("Upload a Dataset", type=["csv", "txt"])
        if data is not None:
           df = pd.read_csv(data)
           st.dataframe(df.head())


			# Model Building
           X = df.iloc[:,0:-1]
           Y = df.iloc[:,-1]
           seed = 7
           # prepare models
           models = []
           models.append(('LR', LogisticRegression()))
           models.append(('LDA', LinearDiscriminantAnalysis()))
           models.append(('KNN', KNeighborsClassifier()))
           models.append(('CART', DecisionTreeClassifier()))
           models.append(('NB', GaussianNB()))
           models.append(('SVM', SVC()))
           # evaluate each model in turn
           model_names = []
           model_mean = []
           model_std = []
           all_models = []
           scoring = 'accuracy'
           for name, model in models:
               kfold = model_selection.KFold(n_splits=10, random_state=seed)
               cv_results = model_selection.cross_val_score(model, X, Y, cv=kfold, scoring=scoring)
               model_names.append(name)
               model_mean.append(cv_results.mean())
               model_std.append(cv_results.std())
               accuracy_results = {"model name":name,"model_accuracy":cv_results.mean(),"standard deviation":cv_results.std()}
               all_models.append(accuracy_results)
               if st.checkbox("Metrics As Table"):
                   st.dataframe(pd.DataFrame(zip(model_names,model_mean,model_std),columns=["Algo","Mean of Accuracy","Std"]))
               if st.checkbox("Metrics As JSON"):
                   st.json(all_models)

    
    
    elif choice == 'Others':
        st.subheader('some projects')
    
    elif choice == 'About':
        # st.subheader('About')
        
        footer_temp = """
	 <!-- CSS  -->
<!-- Font Awesome -->
<link
  href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css"
  rel="stylesheet"
/>
<!-- Google Fonts -->
<link
  href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap"
  rel="stylesheet"
/>
<!-- MDB -->
<link
  href="https://cdnjs.cloudflare.com/ajax/libs/mdb-ui-kit/3.3.0/mdb.min.css"
  rel="stylesheet"
/>
<script
  type="text/javascript"
  src="https://cdnjs.cloudflare.com/ajax/libs/mdb-ui-kit/3.3.0/mdb.min.js"
></script>
	 <footer style="background-color:#f0f2f6;padding:50px; border-radius:10px" class="page-footer grey darken-4">
	    <div class="container" id="aboutapp">
	      <div>
	        <div class="col l6 s12">
	          <h5 class="white-text">Simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.</h5>
	          <p class="grey-text text-lighten-4">Packages used: Streamlit,Pandas,Pyecharts, Echarts.</p>
	        </div>
	      
	   <div class="col l3 s12">
	        <h2>List of charts Used</h2>

                <ul>
                <li>BarChart</li>
                <li>TreeMap</li>
                <li>Rose Chart</li>
                <li>Map Chart</li>
                </ul>  
	    </div>
   
	    <div style="text-align:center"; class="footer-copyright">
	      <div class="container">
	     <div class="container p-4 pb-0">
    <!-- Section: Social media -->
    <section class="mb-4">
      <!-- Facebook -->
      <a
        class="btn btn-primary btn-floating m-1"
        style="background-color: #3b5998;"
        href="#!"
        role="button"
        ><i class="fab fa-facebook-f"></i
      ></a>

      <!-- Twitter -->
      <a
        class="btn btn-primary btn-floating m-1"
        style="background-color: #55acee;"
        href="#!"
        role="button"
        ><i class="fab fa-twitter"></i
      ></a>

      <!-- Google -->
      <a
        class="btn btn-primary btn-floating m-1"
        style="background-color: #dd4b39;"
        href="#!"
        role="button"
        ><i class="fab fa-google"></i
      ></a>

      <!-- Instagram -->
      <a
        class="btn btn-primary btn-floating m-1"
        style="background-color: #ac2bac;"
        href="#!"
        role="button"
        ><i class="fab fa-instagram"></i
      ></a>

      <!-- Linkedin -->
      <a
        class="btn btn-primary btn-floating m-1"
        style="background-color: #0082ca;"
        href="#!"
        role="button"
        ><i class="fab fa-linkedin-in"></i
      ></a>
      <!-- Github -->
      <a
        class="btn btn-primary btn-floating m-1"
        style="background-color: #333333;"
        href="#!"
        role="button"
        ><i class="fab fa-github"></i
      ></a>
    </section>
    <!-- Section: Social media -->
  </div>
  <!-- Grid container -->

  <!-- Copyright -->
  <div class="text-center p-3"; style="background-color: rgba(0, 0, 0, 0.2);  border-radius:10px;  padding-bottom:50px;">
    © 2021 Copyright
    <a class="text-white" href="https://mdbootstrap.com/"></a>
  </div>
	   
	    </div>
	  </footer>
	"""
        components.html(footer_temp, height=800)
    
    

if __name__ == '__main__':
    main()