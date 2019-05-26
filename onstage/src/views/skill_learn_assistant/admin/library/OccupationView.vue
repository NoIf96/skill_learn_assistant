<template>
  <div>
    <el-card class="animated fadeInLeft" shadow="hover">
      <div id="title_div">
        <span id="title_span" >系统职业库</span>
        <el-button class="mini_btn" size="mini" @click="handleAutoAllIntroduction">自动获取描述</el-button>
        <el-button class="mini_btn" size="mini" @click="handleAdd">添加</el-button>
      </div>
      <el-table :data="table.data" border>
        <el-table-column prop="no" label="序号" width="180"/>
        <el-table-column prop="name" label="名称" width="180"/>
        <el-table-column prop="sort_major.label" label="主类别" width="180"/>
        <el-table-column prop="sort_secondary.label" label="次类别" width="180"/>
        <el-table-column prop="sort_language.label" label="语言类别" width="180"/>
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button size="mini" @click="handleClick(scope.$index, scope.row)">查看</el-button>
            <el-button size="mini" @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
            <el-button size="mini" type="danger" @click="handleDelete(scope.$index, scope.row)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
      <el-pagination
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        :page-size="table.page_size"
        layout="total, sizes, prev, pager, next, jumper"
        :total="table.total">
      </el-pagination>
    </el-card>
    <el-dialog title="详情" :visible.sync="dialog.visible" :modal-append-to-body="false" @close="onCancel('form')">
      <el-form :model="form.data" :rules="rules" ref="form">
        <el-row :gutter="10">
          <el-col :span="10">
            <el-form-item label="技能编号" :label-width="form.label_width" prop="no">
              <el-input v-model="form.data.no" :disabled="form.input_disabled" required=true></el-input>
            </el-form-item>
            <el-form-item label="技能名称" :label-width="form.label_width" prop="name">
              <el-input v-model="form.data.name" :disabled="form.input_disabled"></el-input>
            </el-form-item>
          </el-col>
          <el-col :span=14>
            <el-form-item label="主类别" :label-width="form.label_width" prop="sort_major">
              <el-select v-model="form.data.sort_major" placeholder="请选择主类别" :disabled="form.select_disabled">
                <el-option v-for="item in form.options.sort_major" :label="item.label" :value="item.value" :key="item.value"/>
              </el-select>
            </el-form-item>
            <el-form-item label="次类别" :label-width="form.label_width" prop="sort_secondary">
              <el-select v-model="form.data.sort_secondary" placeholder="请选择次类别" :disabled="form.select_disabled">
                <el-option v-for="item in form.options.sort_secondary" :label="item.label" :value="item.value" :key="item.value"/>
              </el-select>
            </el-form-item>
            <el-form-item label="语言类别" :label-width="form.label_width" prop="sort_language">
              <el-select v-model="form.data.sort_language" placeholder="请选择次类别" :disabled="form.select_disabled">
                <el-option v-for="item in form.options.sort_language" :label="item.label" :value="item.value" :key="item.value"/>
              </el-select>
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <el-col>
            <el-form-item label="描述" :label-width="form.label_width" prop="introduction">
              <el-input type="textarea" :autosize="{ minRows: 2, maxRows: 8}" v-model="form.data.introduction" :disabled="form.input_disabled"></el-input>
            </el-form-item>
          </el-col>
        </el-row>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="onGetIntroduction()">获取描述</el-button>
        <el-button type="primary" @click="onSubmit('form')">确 定</el-button>
        <el-button @click="onCancel('form')">取 消</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import SystemLibraryOccupationApi from '@/apis/skill_learn_assistant/admin/library/OccupationApi';
export default {
  name: 'OccupationLibrary',
  data () {
    return {
      table: {
        data: [],
        total: 0,
        current_page: 1,
        page_size: 10
      },
      dialog: {
        type: 4,
        visible: false
      },
      form: {
        data: {
          no: '',
          name: '',
          sort_major: '1',
          sort_secondary: '1',
          sort_language: '1',
          introduction: ''
        },
        options: {
          sort_major: [],
          sort_secondary: [],
          sort_language: []
        },
        label_width: '120px',
        input_disabled: false,
        select_disabled: false
      },
      rules: {
        no: [
          {required: true, message: '请输入技能编号', trigger: 'blur'}
        ],
        name: [
          {required: true, message: '请输入技能名称', trigger: 'blur'}
        ],
        sort_major: [
          {required: true, message: '请至少选择一个主类别', trigger: 'blur'}
        ],
        sort_secondary: [
          {required: true, message: '请选择一个次类别', trigger: 'blur'}
        ],
        sort_language: [
          {required: true, message: '请至少选择一个语言类别', trigger: 'blur'}
        ]
      }
    }
  },
  mounted: function () {
    this.getSortOptions();
    this.getOccupationList();
  },
  methods: {
    getSortOptions () {
      let that = this;
      SystemLibraryOccupationApi.getSortOptions().then(function (result) {
        that.form.options.sort_major = result.data.options.sort_major;
        that.form.options.sort_secondary = result.data.options.sort_secondary;
        that.form.options.sort_language = result.data.options.sort_language;
        console.info(that.form.options)
      }).catch(function (error) {
        console.log(error);
      });
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
    handleSizeChange: function (pageSize) {
      this.table.page_size = pageSize;
      this.getOccupationList();
    },
    handleCurrentChange: function (currentPage) {
      this.table.current_page = currentPage;
      this.getOccupationList();
    },
    handleAdd () {
      this.dialog.type = 1;
      this.dialog.visible = true;
      this.form.input_disabled = false;
      this.form.select_disabled = false;
    },
    handleDelete (index, row) {
      this.dialog.type = 2;
      this.dialog.visible = true;
      this.form.input_disabled = true;
      this.form.select_disabled = true;
      this.getFormData(row);
      console.log(index, row);
    },
    handleEdit (index, row) {
      this.dialog.type = 3;
      this.dialog.visible = true;
      this.form.input_disabled = false;
      this.form.select_disabled = false;
      this.getFormData(row);
      console.log(index, row);
    },
    handleClick (index, row) {
      this.dialog.type = 4;
      this.dialog.visible = true;
      this.form.input_disabled = true;
      this.form.select_disabled = true;
      this.getFormData(row);
      console.log(index, row);
    },
    handleAutoAllIntroduction () {
      SystemLibraryOccupationApi.autoUpdateOccupationIntroduction().then(function (result) {
        alert(result.data.msg);
        this.getSkillList();
      }).catch(function (error) {
        console.log(error);
      });
    },
    onGetIntroduction () {
      let that = this;
      let params = {
        name: that.form.data.name,
        introduction: that.form.data.introduction
      };
      SystemLibraryOccupationApi.getOccupationIntroduction(params).then(function (result) {
        alert(result.data.msg);
        if (result.success) {
          that.form.data.introduction = result.data.introduction;
        }
      })
    },
    onSubmit (form) {
      let that = this;
      this.$refs[form].validate((valid) => {
        if (valid) {
          let params = {
            no: that.form.data.no,
            name: that.form.data.name,
            sort_major: that.form.data.sort_major,
            sort_secondary: that.form.data.sort_secondary,
            sort_language: that.form.data.sort_language,
            introduction: that.form.data.introduction
          };
          if (this.dialog.type === 1) {
            SystemLibraryOccupationApi.add(params).then(function (result) {
              alert(result.data.msg);
              if (result.success) {
                that.dialog.visible = false;
                that.$refs[form].resetFields();
                that.resetFormData();
                that.getOccupationList();
              }
            }).catch(function (error) {
              console.log(error);
            });
          }
          if (this.dialog.type === 2) {
            SystemLibraryOccupationApi.del(params).then(function (result) {
              alert(result.data.msg);
              if (result.success) {
                that.dialog.visible = false;
                that.$refs[form].resetFields();
                that.resetFormData();
                that.getOccupationList();
              }
            }).catch(function (error) {
              console.log(error);
            });
          }
          if (this.dialog.type === 3) {
            SystemLibraryOccupationApi.edit(params).then(function (result) {
              alert(result.data.msg);
              if (result.success) {
                that.dialog.visible = false;
                that.$refs[form].resetFields();
                that.resetFormData();
                that.getOccupationList();
              }
            }).catch(function (error) {
              console.log(error);
            });
          }
          if (this.dialog.type === 4) {
            that.dialog.visible = false;
            that.$refs[form].resetFields();
            that.resetFormData();
            that.getOccupationList();
          }
        } else {
          console.log('error submit!!');
        }
      });
    },
    onCancel (form) {
      this.dialog.visible = false;
      this.$refs[form].resetFields();
      this.resetFormData();
    },
    getFormData (row) {
      this.form.data.no = row.no;
      this.form.data.name = row.name;
      this.form.data.sort_major = row.sort_major.value;
      this.form.data.sort_secondary = row.sort_secondary.value;
      this.form.data.sort_language = row.sort_language.value;
      this.form.data.introduction = row.introduction;
    },
    resetFormData () {
      this.form.data.no = '';
      this.form.data.name = '';
      this.form.data.sort_major = '1';
      this.form.data.sort_secondary = '1';
      this.form.data.sort_language = '1';
      this.form.data.introduction = '';
    }
  }
}
</script>

<style scoped>
  .el-card {
    padding: 10px;
  }
  .el-table {
    width: auto;
    margin-bottom: 20px;
  }
  .mini_btn {
    float: right;
    padding-right: 20px;
  }
  #title_div {
    margin-bottom: 30px;
  }
  #title_span {
    float: left;
    padding-left: 10px;
  }
</style>
