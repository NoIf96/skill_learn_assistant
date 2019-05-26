<template>
  <div id="whole" style="width: 100%">
    <el-card class="animated fadeInLeft" shadow="hover" body-style="height: 290px; position: relative;">
      <span>系统技能库</span>
        <el-row :gutter="10" v-for="i in table.rows" :key="i">
          <el-col :span="4" v-for="j in table.cols" :key="j" v-if="isTableData(i, j)">
            <div  v-on:click="onAddUserData(getOneDate(i, j))">
              <el-popover
                placement="top-end"
                title="描述"
                width="300"
                trigger="hover"
                open-delay=1500
                :content="getOneDate(i, j).introduction">
                <el-card shadow="hover" slot="reference" class="skill">
                  <p>{{getOneDate(i, j).name}}</p>
                </el-card>
              </el-popover>
            </div>
          </el-col>
        </el-row>
        <el-pagination
          @size-change="handleSizeChange"
          @current-change="handleCurrentChange"
          :page-size="table.page_size"
          layout="total, prev, pager, next, jumper"
          :total="table.total"
          style="position: absolute; bottom: 5px; width: 100%">
        </el-pagination>
    </el-card>
    <el-card class="animated fadeInRight" shadow="hover" body-style="height: 300px">
      <span>用户技能</span>
      <el-tooltip class="item" effect="dark" content="更新用户技能" placement="bottom-start">
        <el-button id="add_btn" type="primary" icon="el-icon-check" circle @click="onSaveUserSkill()"></el-button>
      </el-tooltip>
      <el-row :gutter="10" v-for="i in table.rows" :key="i">
        <el-col :span="4" v-for="j in table.cols" :key="j" v-if="isTableUserData(i, j)">
          <div v-on:click="onDelUserData(getOneUserDate(i, j))">
            <el-card shadow="hover" class="skill">
              <p>{{getOneUserDate(i, j).name}}</p>
            </el-card>
          </div>
        </el-col>
      </el-row>
      <el-pagination
        @size-change="handleUserSizeChange"
        @current-change="handleUserCurrentChange"
        :page-size="table.user_page_size"
        layout="total, prev, pager, next, jumper"
        :total="table.user_data.length"
        style="position: absolute; bottom: 5px; width: 100%">
      </el-pagination>
    </el-card>
  </div>
</template>

<script>
import LibrarySkillApi from '@/apis/skill_learn_assistant/admin/library/SkillApi';
import SystemLibrarySkillApi from '@/apis/skill_learn_assistant/ordinary/system_library/SkillApi';
export default {
  name: 'SkillSystemLibrary',
  data () {
    return {
      table: {
        data: [],
        user_data: [],
        total: 0,
        rows: [0, 1],
        cols: [0, 1, 2, 3, 4, 5],
        current_page: 1,
        user_current_page: 1,
        page_size: 12,
        user_page_size: 12
      }
    }
  },
  mounted: function () {
    this.autoCalculatePageSize();
    this.getSkillList();
    this.getUserSkillList();
  },
  methods: {
    autoCalculatePageSize () {
      this.table.page_size = this.table.rows.length * this.table.cols.length;
      this.table.user_page_size = this.table.rows.length * this.table.cols.length;
    },
    handleSizeChange (pageSize) {
      this.table.page_size = pageSize;
      this.getSkillList();
    },
    handleUserSizeChange (pageSize) {
      this.table.user_page_size = pageSize;
    },
    handleCurrentChange (currentPage) {
      this.table.current_page = currentPage;
      this.getSkillList();
    },
    handleUserCurrentChange (currentPage) {
      this.table.user_current_page = currentPage;
    },
    getSkillList () {
      let that = this;
      let params = {
        current_page: that.table.current_page,
        page_size: that.table.page_size
      };
      SystemLibrarySkillApi.getList(params).then(function (result) {
        that.table.data = result.data.list;
        that.table.total = result.total;
      }).catch(function (error) {
        console.log(error);
      });
    },
    getUserSkillList () {
      let that = this;
      let params = {
        current_page: that.table.user_current_page,
        page_size: that.table.user_page_size
      };
      SystemLibrarySkillApi.getUserList(params).then(function (result) {
        that.table.user_data = result.data.list;
        that.table.user_total = result.total;
      }).catch(function (error) {
        console.log(error);
      });
    },
    getSortOptions () {
      let that = this;
      LibrarySkillApi.getSortOptions().then(function (result) {
        that.form.options.sort_major = result.data.options.sort_major;
        that.form.options.sort_secondary = result.data.options.sort_secondary;
        that.form.options.sort_language = result.data.options.sort_language;
        console.info(that.form.options)
      }).catch(function (error) {
        console.log(error);
      });
    },
    getOneDate (i, j) {
      return this.table.data[i * this.table.cols.length + j]
    },
    getOneUserDate (i, j) {
      let skip = (this.table.user_current_page - 1) * this.table.cols.length * this.table.rows.length;
      return this.table.user_data[this.table.user_current_page * i * this.table.cols.length + j + skip]
    },
    isTableData (i, j) {
      return i * this.table.cols.length + j < this.table.data.length ? 1 : 0;
    },
    isTableUserData (i, j) {
      let skip = (this.table.user_current_page - 1) * this.table.cols.length * this.table.rows.length;
      return this.table.user_current_page * i * this.table.cols.length + j + skip < this.table.user_data.length ? 1 : 0;
    },
    onAddUserData (item) {
      let flag = this.find_item(item, this.table.user_data);
      if (flag !== -1) {
        this.table.user_data.splice(flag, 1);
      } else {
        this.table.user_data.push(item);
      }
    },
    onSaveUserSkill () {
      let that = this;
      let skillList = that.table.user_data.map(function (item) {
        return item['no'];
      });
      let params = {
        skill_list: skillList
      };
      SystemLibrarySkillApi.saveUserSkill(params).then(function (result) {
        alert(result.data.msg);
      }).catch(function (error) {
        console.log(error);
      });
    },
    onDelUserData (name) {
      this.table.user_data.splice(this.find_item(name, this.table.user_data), 1);
    },
    find_item (search, array) {
      for (let i = 0; i < array.length; i++) {
        if (search.no === array[i].no) return i;
      }
      return -1;
    }
  }
}
</script>

<style scoped>
  .el-card .skill{
    border-radius: 70px !important;
    width: 110px !important;
    height: 110px !important;
    margin-bottom: 12px;
    border: 1px solid #93969b;
    animation: circular_card 1s linear;
  }
  #add_btn {
    float: right;
  }
  @keyframes circular_card {
    0% {
      filter: alpha(opacity=0);
      opacity: 0;
      margin-top: -30px;
      margin-left: -30px;
    }
    20% {
      filter: alpha(opacity=0.2);
      opacity: 0.2;
      margin-top: -20px;
      margin-left: -20px;
    }
    40% {
      filter: alpha(opacity=0.4);
      opacity: 0.4;
      margin-top: -15px;
      margin-left: -15px;
    }
    60% {
      filter: alpha(opacity=0.6);
      opacity: 0.6;
      margin-top: -10px;
      margin-left: -10px;
    }
    80% {
      filter: alpha(opacity=0.8);
      opacity: 0.8;
      margin-top: -5px;
      margin-left: -5px;
    }
    100% {
      filter: alpha(opacity=1);
      margin-top: 0;
      margin-left: 0;
      opacity: 1;
    }
  }
</style>
