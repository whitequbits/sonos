<template>
  <div class="home">
    <div class="container mx-auto d-flex justify-content-around flex-wrap" v-if="loaded">
      <Card v-for="(stock, index) in this.$store.state.filteredStockSymbol" :key="index" v-bind:symbol="stock['Symbol'].slice(0, 4)" v-bind:name="stock['Company Name']"/>
    </div>
    <div class="loading-card text-center" v-else>
      <div class="spinner-border" style="width: 5rem; height: 5rem;" role="status">
        <span class="sr-only">Loading...</span>
      </div>
    </div>
  </div>
</template>

<script>
import Card from '@/components/Card'

export default {
  name: 'StockList',
  components: {
    Card
  },
    data() {
    return {
      loaded: false,
      errors: []
    }
  },
  mounted() {
    this.loaded = false;
    this.getStockSymbolData()
  },
  methods: {
    getStockSymbolData: function() {
      this.$axios
      .get(`${process.env.VUE_APP_BACKEND_API}/stock_symbol`)
      .then(response => {
        console.log(response.data[0]["Company Name"]);
        this.$store.state.stockSymbol = response.data;
        this.$store.state.filteredStockSymbol = response.data;
        this.loaded = true;
      });
    }
  }
}
</script>

<style scoped>
  .loading-card {
    margin-top: 20%;
    margin-bottom: 20%;
  }
</style>
