<template>
  <div class="my-auto">
    <section class="home-carousel">
      <div id="carouselExampleControls" class="carousel slide" data-ride="carousel">
        <div class="carousel-inner">
          <div class="carousel-item active">
            <img class="d-block w-100" src="https://api.time.com/wp-content/uploads/2020/03/stock-market-coronavirus-2.jpg" alt="First slide">
          </div>
        </div>
      </div>
    </section>
  
    <section class="container icons-carousel">
      <h2 class="my-4">Sonos: Predict your Favorite Stock</h2>
      <h4 class="my-c-25">Our Current Top Pick</h4>
      <div class="d-flex justify-content-around flex-wrap">
        <HomeCard symbol="INDF" src="https://akcdn.detik.net.id/visual/2015/01/04/a2c5f53f-bf4b-4eff-9e4f-773e879068d8_169.jpg?w=650"/>
        <HomeCard symbol="TLKM" src="https://1.bp.blogspot.com/-Gn82eHdGkg8/XVyoNbAlrgI/AAAAAAAANuQ/PyNo1t2DpiwYFxzIDEk9H8oCe_NNTs9PQCLcBGAs/s1600/logo%2Btelkom.png"/>
        <HomeCard symbol="BBRI" src= "https://mmc.tirto.id/image/otf/700x0/2016/05/11/LogoBRI_050_ratio-16x9.JPG"/>
      </div>
   </section>

   <footer class="py-2 bg-dark">
    <div class="container">
      <p class="m-0 text-center text-white">Sonos Project &copy; 2020</p>
    </div>
    <!-- /.container -->
  </footer>
  </div>
</template>

<script>
import HomeCard from '@/components/HomeCard'

export default {
  name: 'Home',
  components: {
    HomeCard
  }
}
</script>

<style scoped>
  footer {
    margin-top: 2%;
  }
  img {
    float: left;
    width:  100px;
    height: 300px;
    object-fit: cover;
  }
</style>
