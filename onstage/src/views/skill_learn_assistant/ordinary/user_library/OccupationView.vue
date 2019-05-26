<template>
  <div>
    <el-card class="animated zoomIn" shadow="hover" body-style="height: 580px; position: relative;">
      <span>推荐职业库</span>
      <br/>
      <br/>
      <el-row :gutter="10" v-for="i in table.rows" :key="i">
        <el-col :span="8" v-for="j in table.cols" :key="j" v-if="isTableData(i, j)">
          <el-card style="height: 500px" shadow="always">
            <div>
              {{ getOneDate(i, j).name }}
            </div>
            <br/>
            <div style="border: 1px solid #93969b; border-radius: 15px; height: 400px">
              {{ getOneDate(i, j).introduction }}
            </div>
            <br/>
          </el-card>
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
import UserLibraryOccupationApi from '@/apis/skill_learn_assistant/ordinary/user_library/OccupationApi';
export default {
  name: 'OccupationUserLibrary',
  data () {
    return {
      table: {
        data: [],
        total: 0,
        rows: [0],
        cols: [0, 1, 2],
        current_page: 1,
        page_size: 3
      }
    }
  },
  mounted: function () {
    this.autoCalculatePageSize();
    this.getUserOccupationList();
  },
  methods: {
    autoCalculatePageSize () {
      this.table.page_size = this.table.rows.length * this.table.cols.length;
    },
    handleSizeChange (pageSize) {
      this.table.page_size = pageSize;
      this.getUserOccupationList();
    },
    handleCurrentChange (currentPage) {
      this.table.current_page = currentPage;
      this.getUserOccupationList();
    },
    getUserOccupationList () {
      let that = this;
      let params = {
        current_page: that.table.current_page,
        page_size: that.table.page_size
      };
      UserLibraryOccupationApi.getUserList(params).then(function (result) {
        that.table.data = result.data.list;
        that.table.total = result.total;
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
</style>
