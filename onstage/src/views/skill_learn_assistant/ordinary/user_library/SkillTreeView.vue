<template>
  <div>
    <el-card>
      <el-radio-group v-model="sort_type" border="true" @change="drawImg">
        <el-radio label="sort_major">主分类</el-radio>
        <el-radio label="sort_secondary">次分类</el-radio>
        <el-radio label="sort_language">语言</el-radio>
      </el-radio-group>
      <br/>
      <br/>
      <el-card id="chart_skill_tree" class="animated zoomIn" style="width: 1200px; height: 550px;">
      </el-card>
    </el-card>
  </div>
</template>

<script>
import UserLibrarySkillTreeApi from '@/apis/skill_learn_assistant/ordinary/user_library/SkillTreeApi';
export default {
  name: 'SkillTreeView',
  data () {
    return {
      graph_data: {},
      sort_type: 'sort_major',
      img_loading: true
    }
  },
  mounted: function () {
    this.drawImg();
  },
  methods: {
    drawImg () {
      let that = this;
      let params = {
        sort_type: that.sort_type
      };
      UserLibrarySkillTreeApi.getList(params).then(function (result) {
        that.graph_data = result.data.graph_data;
        let chartSkillTree = that.$echarts.init(document.getElementById('chart_skill_tree'));
        let option = {
          title: {
            text: '技能树',
            top: 'top',
            left: 'center'
          },
          legend: [{
            top: 30,
            data: that.graph_data.categories.map(function (a) {
              return a.name;
            })
          }],
          animationEasingUpdate: 'quinticInOut',
          animationDuration: 1500,
          series: [{
            name: '技能树',
            type: 'graph',
            layout: 'force',
            data: that.graph_data.nodes,
            links: that.graph_data.links,
            categories: that.graph_data.categories,
            roam: true,
            focusNodeAdjacency: true,
            label: {
              normal: {
                show: true,
                position: 'right',
                formatter: function (params) {
                  return params.data.label;
                }
              }
            },
            itemStyle: {
              normal: {
                opacity: 0.9,
                borderColor: '#fff',
                borderWidth: 1,
                shadowBlur: 10,
                shadowColor: 'rgba(0, 0, 0, 0.3)'
              }
            },
            // 关系边的公用线条样式
            lineStyle: {
              normal: {
                show: true,
                color: 'source',
                curveness: 0.3
              }
            },
            emphasis: {
              lineStyle: {
                width: 5
              },
              itemStyle: {
                borderWidth: 2
              }
            },
            force: {
              edgeLength: [100, 200],
              repulsion: 100
            }

          }]
        };
        chartSkillTree.setOption(option);
      }).catch(function (error) {
        console.log(error);
      });
    }
  }
}
</script>
<style scoped>
  #chart_skill_tree {
    background: url('../../../../assets/img/humans-background-op30.png') center center no-repeat;
    /*background-size:100% 100%;*/
  }
</style>
