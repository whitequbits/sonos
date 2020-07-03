<template>
  <div class="home">
    <Card v-for="(stock, index) in stockData" :key="index" v-bind:text="stock.title"/>
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
      stockData: [],
      errors: []
    }
  },
  mounted: function () {
    this.getStockData()
  },
  methods: {
    async getStockData () {
      this.$axios
        .get('https://my-json-server.typicode.com/typicode/demo/posts')
        .then( response => {
          this.stockData = response.data
        })
    }
  }
}
</script>
