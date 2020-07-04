<template>
  <div class="stock-detail">
    <div class="container">
      <StockCard class="mx-auto" :symbol="$route.params.symbol"/>
      <Table class="mx-auto"/>
    </div>
  </div>
</template>

<script>
import Table from '@/components/Table'
import StockCard from '@/components/StockCard'

export default {
  name: 'StockDetail',
  components: { 
    Table,
    StockCard
  },
  props: {
    symbol: String
  }
}
</script>

<style scoped>
  .container {
    margin-top: 2%;
  }
</style>
