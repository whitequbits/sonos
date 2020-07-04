<template>
  <div>
    <b-navbar toggleable="lg" type="dark" variant="danger">
      <b-navbar-brand href="/">Sonos</b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <router-link to="/">Home</router-link>
          <router-link to="/about">About</router-link>
        </b-navbar-nav>
        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto mr-5">
          <b-nav-form v-if="this.$route.path == '/'">
            <b-form-input @input="search_text()" size="sm" class="mr-sm-2" placeholder="Search" v-model="search.text"></b-form-input>
          </b-nav-form>
          <b-nav-form v-else="">
            <router-link to="/">Back</router-link>
          </b-nav-form>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>
export default {
  name: 'Navigation',
  data() {
    return {
      search: { text: "" },
    }
  },
  methods: {
    search_text() {
      var inside = this;
      this.$store.state.filteredStockSymbol = this.$store.state.stockSymbol.filter(function(stockSymbol) {
        if (
          stockSymbol.symbol
            .toLowerCase()
            .indexOf(inside.search.text.toLowerCase()) != "-1"
        ) {
          return stockSymbol;
        }
      });
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  a {
    color: white;
    margin-left: 6px;
    margin-right: 6px;
  }

  a:hover {
    color: white;
  }

  b-navbar {
    background-color: white;
  }
</style>
