<template>
  <div :key="$route.path">
      <el-card id="main_card" class="animated flipInX">
        <el-row :gutter="10">
          <el-col :span="8">
            <div id="config_block" class="block">
              <h3 class="demonstration">模型参数</h3>
              <el-form :model="form.data" label-width="80px" label-position="right"  ref="form">
                <el-card>
                  <el-carousel trigger="click" height="500px">
                    <el-carousel-item v-for="item in 2" :key="item">
                      <template v-if="item === 1">
                        <el-card shadow="hover">
                          <h3>k聚类模型参数</h3>
                          <div>
                            <el-form-item label="n_clusters" prop="n_clusters">
                              <el-input v-model="form.data.kmeans.n_clusters" placeholder="聚类数" required=true></el-input>
                            </el-form-item>
                            <el-form-item label="max_iter" prop="max_iter">
                              <el-input v-model="form.data.kmeans.max_iter" placeholder="最大迭代次数" required=true></el-input>
                            </el-form-item>
                            <el-form-item label="n_init" prop="n_init">
                              <el-input v-model="form.data.kmeans.n_init" placeholder="初始质心数" required=true></el-input>
                            </el-form-item>
                            <el-form-item label="init" prop="init">
                              <el-select v-model="form.data.kmeans.init" placeholder="请选择初始值选择方式">
                                <el-option v-for="item in form.options.kmeans.init" :label="item" :value="item" :key="item"/>
                              </el-select>
                            </el-form-item>
                            <el-form-item label="algorithm" prop="algorithm">
                              <el-select v-model="form.data.kmeans.algorithm" placeholder="请选择算法">
                                <el-option v-for="item in form.options.kmeans.algorithm" :label="item" :value="item" :key="item"/>
                              </el-select>
                            </el-form-item>
                          </div>
                        </el-card>
                      </template>
                      <template v-if="item === 2">
                        <el-card shadow="hover">
                          <h3>k近邻模型参数</h3>
                          <div>
                            <el-form-item label="n_neighbors" prop="n_neighbors">
                              <el-input v-model="form.data.knn.n_neighbors" required=true></el-input>
                            </el-form-item>
                            <el-form-item label="radius" prop="radius">
                              <el-input v-model="form.data.knn.radius" required=true></el-input>
                            </el-form-item>
                            <el-form-item label="algorithm" prop="algorithm">
                              <el-select v-model="form.data.knn.algorithm" placeholder="请选择算法">
                                <el-option v-for="item in form.options.knn.algorithm" :label="item" :value="item" :key="item"/>
                              </el-select>
                            </el-form-item>
                          </div>
                        </el-card>
                      </template>
                    </el-carousel-item>
                  </el-carousel>
                  <el-button plain v-loading.fullscreen.lock="full_screen_gen_loading"
                             element-loading-text="模型生成中"
                             element-loading-spinner="el-icon-loading"
                             element-loading-background="rgba(0, 0, 0, 0.2)"  @click="onGenerateModel('form')">生成模型</el-button>
                  <el-button plain @click="onInputModelName">保存模型</el-button>
                  <el-button plain @click="onSelectModel">加载模型</el-button>
                </el-card>
              </el-form>
            </div>
          </el-col>
          <el-col :span="16">
            <div id="config_view">
              <el-card
                v-loading="img_loading"
                element-loading-text="数据图加载中"
                element-loading-spinner="el-icon-loading"
                element-loading-background="rgba(0, 0, 0, 0.2)">
                <el-carousel :interval="4000" type="card" height="575px" >
                  <el-carousel-item v-for="(item, index) in image_datas" :key="index">
                    <h3> {{ item.title }} </h3>
                    <div :id="'chart_' + item.title" style="width: 400px; height: 500px; "></div>
                  </el-carousel-item>
                </el-carousel>
              </el-card>
            </div>
          </el-col>
        </el-row>
      </el-card>
      <el-dialog title="模型名称" :visible.sync="dialog_save_model_visible" :modal-append-to-body="false" width="300px">
        <el-form :model="form.save_model" ref="form">
          <el-form-item label="请输入模型名称">
            <el-input v-model="form.save_model.name" autocomplete="off"></el-input>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button type="primary" v-loading.fullscreen.lock="full_screen_save_loading"
                     element-loading-text="模型保存中"
                     element-loading-spinner="el-icon-loading"
                     element-loading-background="rgba(0, 0, 0, 0.2)" @click="onSaveModel('form')">确 定</el-button>
          <el-button @click="resetFormSave_model()">取 消</el-button>
        </div>
      </el-dialog>
      <el-dialog title="选择模型" :visible.sync="dialog_load_model_visible" :modal-append-to-body="false" width="300px">
        <el-form :model="form.load_model" ref="form">
          <el-form-item label="请选择模型">
            <el-select v-model="form.load_model.name" placeholder="请选择模型">
              <el-option
                v-for="item in model_list" :key="item" :label="item" :value="item">
              </el-option>
            </el-select>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button type="primary" v-loading.fullscreen.lock="full_screen_load_loading"
                     element-loading-text="模型保存中"
                     element-loading-spinner="el-icon-loading"
                     element-loading-background="rgba(0, 0, 0, 0.2)" @click="onLoadModel('form')">确 定</el-button>
          <el-button @click="resetFormLoad_model()">取 消</el-button>
        </div>
      </el-dialog>
  </div>
</template>

<script>
import SystemSystemConfigApi from '@/apis/skill_learn_assistant/admin/system/ConfigApi';
export default {
  name: 'ConfigSystem',
  data () {
    return {
      model_type: this.$route.meta.model_type,
      config_items: ['kmeans_card', 'knn_card'],
      form: {
        data: {
          kmeans: {
            n_clusters: 0,
            max_iter: 0,
            n_init: 0,
            init: '',
            algorithm: ''
          },
          knn: {
            n_neighbors: 0,
            radius: 0,
            algorithm: ''
          },
          label_width: '50px'
        },
        options: {
          kmeans: {
            init: [],
            algorithm: []
          },
          knn: {
            algorithm: []
          }
        },
        save_model: {
          name: ''
        },
        load_model: {
          name: ''
        }
      },
      image_datas: [{title: 'elbow_rule', data: []}, {title: 'plt2d', data: []}, {title: 'plt3d', data: []}],
      model_list: [],
      dialog_save_model_visible: false,
      dialog_load_model_visible: false,
      full_screen_gen_loading: false,
      full_screen_save_loading: false,
      full_screen_load_loading: false,
      img_loading: true
    }
  },
  mounted: function () {
    this.getModelType();
    this.getModelParamOptions();
    this.getModelParam();
    this.getImgData();
  },
  watch: {
    $route: {
      handler: function (val, oldVal) {
        this.getModelType();
        this.getModelParamOptions();
        this.getModelParam();
        this.getImgData();
      }
    }
  },
  updated: function () {
    this.drawImg();
  },
  methods: {
    getModelType () {
      let that = this;
      that.model_type = that.$route.meta.model_type;
    },
    getModelParamOptions () {
      let that = this;
      SystemSystemConfigApi.getModelParamOptions().then(function (result) {
        that.form.options.kmeans = result.data.options.kmeans;
        that.form.options.knn = result.data.options.knn;
      }).catch(function (error) {
        console.log(error);
      });
    },
    getModelList () {
      let that = this;
      let params = {
        model_type: that.model_type
      };
      SystemSystemConfigApi.getModelList(params).then(function (result) {
        that.model_list = result.data.list;
      }).catch(function (error) {
        console.log(error);
      });
    },
    getModelParam () {
      let that = this;
      let params = {
        model_type: that.model_type
      };
      SystemSystemConfigApi.getModelParam(params).then(function (result) {
        that.form.data.kmeans = result.data.kmeans;
        that.form.data.knn = result.data.knn;
      }).catch(function (error) {
        console.log(error);
      });
    },
    onGenerateModel (form) {
      let that = this;
      that.full_screen_gen_loading = true;
      this.$refs[form].validate((valid) => {
        if (valid) {
          let kmeans = {
            'n_clusters': Number(that.form.data.kmeans.n_clusters),
            'max_iter': Number(that.form.data.kmeans.max_iter),
            'n_init': Number(that.form.data.kmeans.n_init),
            'init': that.form.data.kmeans.init,
            'algorithm': that.form.data.kmeans.algorithm
          };
          let knn = {
            'n_neighbors': Number(that.form.data.knn.n_neighbors),
            'radius': Number(that.form.data.knn.radius),
            'algorithm': that.form.data.knn.algorithm
          };
          let params = {
            model_type: that.model_type,
            kmeans: kmeans,
            knn: knn
          };
          SystemSystemConfigApi.generateModel(params).then(function (result) {
            that.full_screen_gen_loading = false;
            if (result.data.code === 1) {
              that.getImgData();
              alert(result.data.msg);
            } else {
              alert(result.data.msg);
            }
          }).catch(function (error) {
            console.log(error);
          });
        }
      });
    },
    onInputModelName () {
      this.dialog_save_model_visible = true
    },
    onSaveModel (form) {
      let that = this;
      that.full_screen_save_loading = true;
      this.$refs[form].validate((valid) => {
        that.full_screen_save_loading = false;
        if (valid) {
          let params = {
            model_type: that.model_type,
            model_name: that.form.save_model.name
          };
          SystemSystemConfigApi.saveModel(params).then(function (result) {
            alert(result.data.msg);
            that.resetFormSave_model();
          }).catch(function (error) {
            console.log(error);
          });
        }
      })
    },
    onLoadModel (form) {
      let that = this;
      that.full_screen_load_loading = true;
      this.$refs[form].validate((valid) => {
        that.full_screen_load_loading = false;
        if (valid) {
          let params = {
            model_type: that.model_type,
            model_name: that.form.load_model.name
          };
          SystemSystemConfigApi.loadModel(params).then(function (result) {
            alert(result.data.msg);
            that.resetFormLoad_model();
            that.getModelParam();
          }).catch(function (error) {
            console.log(error);
          });
        }
      })
    },
    onSelectModel () {
      let that = this;
      that.getModelList();
      that.dialog_load_model_visible = true;
    },
    getImgData () {
      let that = this;
      let params = {
        model_type: that.model_type
      };
      SystemSystemConfigApi.getImgData(params).then(function (result) {
        that.image_datas = result.data.list;
      }).catch(function (error) {
        console.log(error);
      });
    },
    resetFormSave_model () {
      this.dialog_save_model_visible = false;
      this.form.save_model.name = '';
    },
    resetFormLoad_model () {
      this.dialog_load_model_visible = false;
      this.form.load_model.name = '';
    },
    drawImg () {
      let that = this;
      let chartElbowRule = this.$echarts.init(document.getElementById('chart_elbow_rule'));
      let chartPlt2d = this.$echarts.init(document.getElementById('chart_plt2d'));
      let chartPlt3d = this.$echarts.init(document.getElementById('chart_plt3d'));
      chartElbowRule.setOption(that.drawElowRuleOption(), true);
      chartPlt2d.setOption(this.drawPlt2dOption(), true);
      chartPlt3d.setOption(this.drawPlt3dOption(), true);

      window.addEventListener('resize', function () { chartElbowRule.resize() });
      window.addEventListener('resize', function () { chartPlt2d.resize() });
      window.addEventListener('resize', function () { chartPlt3d.resize() });
      that.img_loading = false;
    },
    drawElowRuleOption () {
      return {
        grid: {
          show: true,
          backgroundColor: 'rgba(200, 200, 200, 0.3)'
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'shadow'
          }
        },
        dataZoom: [
          {
            type: 'slider',
            start: 0,
            end: 100
          }
        ],
        xAxis: {
          name: 'k值',
          nameLocation: 'middle',
          type: 'category',
          data: ['1', '2', '3', '4', '5', '6', '7', '8', '9'],
          axisTick: {
            alignWithLabel: true
          }
        },
        yAxis: [
          {
            type: 'value'
          }
        ],
        series: [
          {
            name: '肘部预测图',
            type: 'line',
            data: this.image_datas[0].data
          }
        ]
      };
    },
    drawPlt2dOption () {
      let legend = [];
      let series = this.image_datas[1].data.map((item, index) => {
        let name = `类别${index + 1}`;
        legend.push(name);
        return {
          name: name,
          data: item,
          type: 'scatter'
        }
      });
      return {
        grid: {
          show: true,
          backgroundColor: 'rgba(200, 200, 200, 0.3)'
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'shadow'
          }
        },
        dataZoom: [
          {
            type: 'slider',
            start: 0,
            end: 100
          }
        ],
        legend: {
          y: 'top',
          data: legend
        },
        xAxis: {
          name: '主类别',
          nameLocation: 'middle'
        },
        yAxis: {
          name: '次类别'
        },
        series: series
      };
    },
    drawPlt3dOption () {
      let legend = [];
      let series = this.image_datas[2].data.map((item, index) => {
        let name = `类别${index + 1}`;
        legend.push(name);
        return {
          name: name,
          data: item,
          type: 'scatter3D'
        }
      });
      console.info(series);
      return {
        grid3D: {
          splitArea: {
            show: true,
            areaStyle: {
              color: 'rgba(200, 200, 200, 0.3)'
            }
          }
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'shadow'
          }
        },
        legend: {
          y: 'top',
          data: legend
        },
        xAxis3D: {
          name: '主类别',
          nameLocation: 'middle'
        },
        yAxis3D: {
          name: '次类别',
          nameLocation: 'middle'
        },
        zAxis3D: {
          name: '语言类别',
          nameLocation: 'middle'
        },
        series: series
      };
    }
  }
}
</script>

<style scoped>
  #main_card {
    height: 100%;
  }
  #config_block {
    /*width: 100%;*/
    height: 80%;
  }
  #config_view {
    /*width: 50%;*/
    height: 80%;
  }
</style>
