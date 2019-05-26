<template>
  <div>
    <el-card class="animated zoomIn" shadow="hover">
      <div id="title_div">
        <span id="title_span" >管理员</span>
        <el-button id="add_btn" size="mini" @click="handleAdd">添加</el-button>
      </div>
      <el-row :gutter="10" v-for="i in table.rows" :key="i">
        <el-col :span="8" v-for="j in table.cols" :key="j" v-if="isTableData(i, j)">
          <el-card>
            <div slot="header" class="clearfix">
              <span>管理员信息</span>
              <el-button size="medium" type="text" @click="handleDelete(getOneDate(i, j))" icon="el-icon-close"/>
            </div>
            <el-row><img src="" class="image"></el-row>
            <div>
              <p>姓名：<span>{{getOneDate(i, j).user_name}}</span></p>
              <p>权限：<span>{{getOneDate(i, j).permission.label}}</span></p>
            </div>
            <div>
              <el-button size="mini" @click="handleClick(getOneDate(i, j))">查看</el-button>
              <el-button size="mini" @click="handleEdit(getOneDate(i, j))">编辑</el-button>
            </div>
          </el-card>
        </el-col>
      </el-row>
      <el-pagination
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        :page-size="table.page_size"
        layout="total, prev, pager, next, jumper"
        :total="table.total">
      </el-pagination>
    </el-card>
    <el-dialog title="详情" :visible.sync="dialog.visible" :modal-append-to-body="false" @close="onCancel('form')">
      <el-form :model="form.data" :rules="rules" ref="form">
        <el-row :gutter="10">
          <el-col :span="10">
            <el-form-item label="管理员名称" :label-width="form.label_width" prop="user_name">
              <el-input v-model="form.data.user_name" :disabled="form.input_disabled" required=true></el-input>
            </el-form-item>
            <el-form-item label="管理员密码" :label-width="form.label_width" prop="password" v-if="!form.input_pw_disabled">
              <el-input v-model="form.data.password" :disabled="form.select_disabled" required=true></el-input>
            </el-form-item>
            <el-form-item label="管理员权限" :label-width="form.label_width" prop="permission">
              <el-select v-model="form.data.permission" placeholder="请选择管理员权限" :disabled="form.select_disabled">
                <el-option v-for="item in form.permission_options" :label="item.label" :value="item.value" :key="item.value"/>
              </el-select>
            </el-form-item>
          </el-col>
        </el-row>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button type="primary" @click="onSubmit('form')">确 定</el-button>
        <el-button @click="onCancel('form')">取 消</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import SystemUserAdminApi from '@/apis/skill_learn_assistant/admin/user/AdminApi';
export default {
  name: 'AdminUser',
  data () {
    return {
      table: {
        data: [],
        total: 0,
        rows: [0, 1, 2],
        cols: [0, 1, 2],
        current_page: 1,
        page_size: 9
      },
      dialog: {
        type: 4,
        visible: false
      },
      form: {
        data: {
          user_name: '',
          password: '',
          permission: '2'
        },
        permission_options: [],
        label_width: '120px',
        input_disabled: false,
        input_pw_disabled: false,
        select_disabled: false
      },
      rules: {
        user_name: [
          {required: true, message: '请输入管理员用户名称', trigger: 'blur'}
        ],
        password: [
          {required: true, message: '请输入密码', trigger: 'blur'}
        ],
        permission: [
          {required: true, message: '请选择权限', trigger: 'blur'}
        ]
      }
    }
  },
  mounted: function () {
    this.getPermissionOptions();
    this.getAdminUserList();
  },
  methods: {
    getAdminUserList () {
      let that = this;
      let params = {
        current_page: that.table.current_page,
        page_size: that.table.page_size
      };
      SystemUserAdminApi.getList(params).then(function (result) {
        that.table.data = result.data.list;
        that.table.total = result.total;
      }).catch(function (error) {
        console.log(error);
      });
    },
    getPermissionOptions () {
      let that = this;
      SystemUserAdminApi.getPermissionOptions().then(function (result) {
        that.form.permission_options = result.data.options;
        console.info(that.form.permission_options)
      }).catch(function (error) {
        console.log(error);
      });
    },
    handleSizeChange: function (pageSize) {
      this.table.page_size = pageSize;
      this.getAdminUserList();
    },
    handleCurrentChange: function (currentPage) {
      this.table.current_page = currentPage;
      this.getAdminUserList();
    },
    handleAdd () {
      this.dialog.type = 1;
      this.dialog.visible = true;
      this.form.input_disabled = false;
      this.form.input_pw_disabled = false;
      this.form.select_disabled = false;
    },
    handleDelete (data) {
      this.dialog.type = 2;
      this.dialog.visible = true;
      this.form.input_disabled = true;
      this.form.input_pw_disabled = true;
      this.form.select_disabled = true;
      this.getFormData(data);
      console.log(data);
    },
    handleEdit (data) {
      this.dialog.type = 3;
      this.dialog.visible = true;
      this.form.input_disabled = false;
      this.form.input_pw_disabled = false;
      this.form.select_disabled = false;
      this.getFormData(data);
      console.log(data);
    },
    handleClick (data) {
      this.dialog.type = 4;
      this.dialog.visible = true;
      this.form.input_disabled = true;
      this.form.input_pw_disabled = false;
      this.form.select_disabled = true;
      this.getFormData(data);
      console.log(data);
    },
    onSubmit: function (form) {
      let that = this;
      this.$refs[form].validate((valid) => {
        if (valid) {
          let params = {
            user_name: that.form.data.user_name,
            password: that.form.data.password,
            permission: that.form.data.permission
          };
          if (this.dialog.type === 1) {
            SystemUserAdminApi.add(params).then(function (result) {
              alert(result.data.msg);
              if (result.success) {
                that.dialog.visible = false;
                that.$refs[form].resetFields();
                that.resetFormData();
                that.getAdminUserList();
              }
            }).catch(function (error) {
              console.log(error);
            });
          }
          if (this.dialog.type === 2) {
            SystemUserAdminApi.del(params).then(function (result) {
              alert(result.data.msg);
              if (result.success) {
                that.dialog.visible = false;
                that.$refs[form].resetFields();
                that.resetFormData();
                that.getAdminUserList();
              }
            }).catch(function (error) {
              console.log(error);
            });
          }
          if (this.dialog.type === 3) {
            SystemUserAdminApi.edit(params).then(function (result) {
              alert(result.data.msg);
              if (result.success) {
                that.dialog.visible = false;
                that.$refs[form].resetFields();
                that.resetFormData();
                that.getAdminUserList();
              }
            }).catch(function (error) {
              console.log(error);
            });
          }
          if (this.dialog.type === 4) {
            that.dialog.visible = false;
            that.$refs[form].resetFields();
            that.resetFormData();
            that.getAdminUserList();
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
      this.form.data.user_name = row.user_name;
      this.form.data.password = row.password_hash;
      this.form.data.permission = row.permission.value;
    },
    resetFormData () {
      this.form.data.user_name = '';
      this.form.data.password = '';
      this.form.data.permission = '2';
    },
    getOneDate (i, j) {
      return this.table.data[i * 3 + j]
    },
    isTableData (i, j) {
      return i * 3 + j < this.table.data.length ? 1 : 0;
    }
  }
}
</script>

<style scoped>
  .el-card{
    padding: 10px;
  }
  .el-table{
    width: auto;
    margin-bottom: 20px;
  }
  #title_div {
    margin-bottom: 30px;
  }
  #title_span {
    float: left;
    padding-left: 10px;
  }
  #add_btn {
    float: right;
    padding-right: 20px;
  }
</style>
