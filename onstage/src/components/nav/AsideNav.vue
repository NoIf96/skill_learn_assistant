<!--Aside 左侧导航公共组件-->
<template>
  <!--左侧导航-->
  <div id="aside">
    <!--导航菜单-->
    <el-menu router>
      <template v-for="route in $router.options.routes">
        <template v-if="menu_type === route.name">
          <template v-for="(items, index) in route.children">
            <el-menu-item v-if="items.is_leaf" :index="index+''" :key="items.path" v-show="items.is_menu_show" :route="items.path">
              <span slot="title">{{items.name}}</span>
            </el-menu-item>
            <el-submenu v-else-if="!items.is_leaf" :index="index+''" :key="items.path" v-show="items.is_menu_show">
              <template slot="title"><span slot="title">{{items.name}}</span></template>
              <el-menu-item v-for="(item, i) in items.children" :index="index+'-'+i" :route="item.path"
                            :key="item.path" v-show="item.is_menu_show">
                <span slot="title">{{item.name}}</span>
              </el-menu-item>
            </el-submenu>
          </template>
        </template>
      </template>
    </el-menu>
  </div>
</template>

<script>
export default {
  name: 'AsideNav',
  props: {
    menu_type: String
  }
}

</script>

<style scoped>
  #aside {
    background-color: rgb(230, 230, 230);
    color: #333;
    text-align: left;
    /*line-height: 200px;*/
    opacity: 0.98;
    width: 200px;
    height: auto;
  }
</style>
