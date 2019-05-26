<template>
  <div>
    <el-card class="animated fadeInLeft" shadow="hover" body-style="height: 580px; position: relative;">
      <span>系统职业库</span>
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
                  <p style="margin-top: 30px">{{getOneDate(i, j).name}}</p>
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
          style="position: absolute; bottom: 10px; width: 100%">
        </el-pagination>
    </el-card>
  </div>
</template>

<script>
import LibraryOccupationApi from '@/apis/skill_learn_assistant/admin/library/OccupationApi';
import SystemLibraryOccupationApi from '@/apis/skill_learn_assistant/ordinary/system_library/OccupationApi';
export default {
  name: 'OccupationSystemLibrary',
  data () {
    return {
      table: {
        data: [],
        total: 0,
        rows: [0, 1, 3, 4, 5],
        cols: [0, 1, 2, 3, 4, 5],
        current_page: 1,
        page_size: 36
      }
    }
  },
  mounted: function () {
    this.autoCalculatePageSize();
    this.getOccupationList();
  },
  methods: {
    autoCalculatePageSize () {
      this.table.page_size = this.table.rows.length * this.table.cols.length;
    },
    handleSizeChange (pageSize) {
      this.table.page_size = pageSize;
      this.getOccupationList();
    },
    handleCurrentChange (currentPage) {
      this.table.current_page = currentPage;
      this.getOccupationList();
    },
    getOccupationList () {
      let that = this;
      let params = {
        current_page: that.table.current_page,
        page_size: that.table.page_size
      };
      SystemLibraryOccupationApi.getList(params).then(function (result) {
        that.table.data = result.data.list;
        that.table.total = result.total;
      }).catch(function (error) {
        console.log(error);
      });
    },
    getSortOptions () {
      let that = this;
      LibraryOccupationApi.getSortOptions().then(function (result) {
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
    isTableData (i, j) {
      return i * this.table.cols.length + j < this.table.data.length ? 1 : 0;
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
    width: 120px !important;
    height: 120px !important;
    margin-bottom: 12px;
    border: 1px solid #93969b;
  }
  #add_btn {
    float: right;
  }
</style>
