<template>
  <div class="home">
    <div class="container mx-auto d-flex justify-content-around flex-wrap">
      <Card v-for="(stock, index) in stockSymbol" :key="index" v-bind:symbol="stock.symbol.slice(0, 4)" v-bind:name="stock.description"/>
    </div>
  </div>
</template>

<script>
import Card from '@/components/Card'

export default {
  name: 'Home',
  components: {
    Card
  },
    data() {
    return {
      stockSymbol: [],
      errors: []
    }
  },
  mounted() {
    this.getStockSymbolData()
  },
  methods: {
    getStockSymbolData: function() {
      this.$axios
      .get("http://localhost:8081/stock_symbol")
      .then(response => {
        this.stockSymbol = response.data;
      });
    }
  }
}
</script>
