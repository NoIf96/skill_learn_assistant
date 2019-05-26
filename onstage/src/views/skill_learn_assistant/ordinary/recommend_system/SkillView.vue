<template>
    <el-card style="width: 100%; height: 100%">
      <el-button id="see_btn" v-show="see_btn_show" @click="onSeeSkillList()">查看推荐技能</el-button>
      <br/>
      <br/>
      <div class="animated zoomIn" style="width: 100%; height: 100%" v-show="!tree_show">
        <el-carousel :interval="4000" type="card" height="450px" v-show="carousel_show">
          <el-carousel-item v-for="item in recommend_skill_list" :key="item">
            <el-card style="height: 450px" shadow="always">
              <div>
                {{ item.name }}
              </div>
              <br/>
              <div style="border: 1px solid #93969b; border-radius: 15px; height: 330px;">
                {{ item.introduction }}
              </div>
              <br/>
              <el-button type="primary" @click="onAddUserSkill(item.no)">加入技能</el-button>
            </el-card>
          </el-carousel-item>
        </el-carousel>
        <span slot="footer" class="dialog-footer">
          <el-button type="primary" @click="tree_show = true">确 定</el-button>
        </span>
      </div>
      <div id="chart_recommend_skill_tree" class="animated zoomIn" style="width: 1200px; height: 550px;" v-show="tree_show">
        <el-tooltip class="item" effect="light" content="开始进行推荐" placement="top">
          <el-button id="recommend_btn" class="animated rotateInUpRight" v-show="recommend_btn_show" @click="onGetRecommendedSkill()" circle>
            <img src="../../../../assets/img/humans-background.png"/>
          </el-button>
        </el-tooltip>
      </div>
    </el-card>
</template>

<script>
import RecommendSystemSkillApi from '@/apis/skill_learn_assistant/ordinary/recommend_system/SkillApi';
export default {
  name: 'SkillView',
  data () {
    return {
      recommend_btn_show: true,
      see_btn_show: false,
      carousel_show: false,
      tree_show: true,
      graph_data: {},
      recommend_skill_list: []
    }
  },
  methods: {
    drawImg () {
      let that = this;
      RecommendSystemSkillApi.getRecommendedSkillTree().then(function (result) {
        that.graph_data = result.data.graph_data;
        that.recommend_skill_list = result.data.list;
        let chartSkillTree = that.$echarts.init(document.getElementById('chart_recommend_skill_tree'));
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
    },
    onGetRecommendedSkill () {
      let that = this;
      that.recommend_btn_show = false;
      that.see_btn_show = true;
      that.drawImg();
    },
    onSeeSkillList () {
      let that = this;
      that.carousel_show = true;
      that.tree_show = !that.tree_show;
      that.drawImg();
    },
    onAddUserSkill (no) {
      let that = this;
      let params = {
        no: no
      };
      RecommendSystemSkillApi.getAddUserSkill(params).then(function (result) {
        alert(result.data.msg);
        RecommendSystemSkillApi.getRecommendedSkillTree().then(function (result) {
          that.graph_data = result.data.graph_data;
          that.recommend_skill_list = result.data.list;
        }).catch(function (error) {
          console.log(error);
        });
      }).catch(function (error) {
        console.log(error);
      });
    }
  }
}
</script>

<style scoped>
  #recommend_btn {
     margin-top: 15%;
      box-shadow: 0 2px 4px rgba(0, 0, 0, .8), 0 0 6px rgba(0, 0, 0, .6)
   }
</style>
