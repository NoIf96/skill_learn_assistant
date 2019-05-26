<template>
    <el-card style="width: 100%; height: 100%">
      <br/>
      <div class="animated zoomIn" style="width: 100%; height: 100%" v-show="!tree_show">
        <el-carousel :interval="4000" type="card" height="450px" v-show="carousel_show">
          <el-carousel-item v-for="item in recommend_occupation_list" :key="item">
            <el-card style="height: 450px" shadow="always">
              <div>
                {{ item.name }}
              </div>
              <br/>
              <div style="border: 1px solid #93969b; border-radius: 15px; height: 330px;">
                {{ item.introduction }}
              </div>
              <br/>
              <el-button type="primary" @click="onAddUserRecommendOccupationList(item.no)">加入职业</el-button>
            </el-card>
          </el-carousel-item>
        </el-carousel>
      </div>
      <div class="animated zoomIn" style="width: 1200px; height: 550px;" v-show="tree_show">
        <el-tooltip class="item" effect="light" content="开始进行推荐" placement="top">
          <el-button id="recommend_btn" class="animated rotateInUpLeft" v-show="recommend_btn_show" @click="onGetRecommendedOccupation()" circle>
            <img src="../../../../assets/img/humans-background.png"/>
          </el-button>
        </el-tooltip>
      </div>
    </el-card>
</template>

<script>
import RecommendSystemOccupationApi from '@/apis/skill_learn_assistant/ordinary/recommend_system/OccupationApi';
export default {
  name: 'OccupationView',
  data () {
    return {
      recommend_btn_show: true,
      see_btn_show: false,
      carousel_show: false,
      tree_show: true,
      recommend_occupation_list: []
    }
  },
  methods: {
    getRecommendedOccupationList () {
      let that = this;
      RecommendSystemOccupationApi.getRecommendedOccupationList().then(function (result) {
        that.recommend_occupation_list = result.data.list;
      }).catch(function (error) {
        console.log(error);
      });
    },
    onGetRecommendedOccupation () {
      let that = this;
      that.recommend_btn_show = false;
      that.see_btn_show = true;
      that.getRecommendedOccupationList();
      that.onSeeSkillList();
    },
    onSeeSkillList () {
      let that = this;
      that.carousel_show = true;
      that.tree_show = !that.tree_show;
    },
    onAddUserRecommendOccupationList (no) {
      let that = this;
      let params = {
        no: no
      };
      RecommendSystemOccupationApi.addUserRecommendOccupationList(params).then(function (result) {
        alert(result.data.msg);
        that.getRecommendedOccupationList();
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
