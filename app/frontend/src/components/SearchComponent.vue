<template>
    <b-container id="search-wrapper">
        <b-row>
            <div class="col-sm-10 offset-sm-1 text-center">
                <div class="input-group mb-3">
                    <input
                        v-model="query"
                        type="text"
                        class="form-control"
                        placeholder="Introduce Twitter Username/Bio"
                        aria-label="Introduce Twitter Username/Bio"
                        aria-describedby="button-addon2"
                    />
                    <div class="input-group-append">
                        <button
                            @click="getProfiles"
                            class="btn btn-outline-primary"
                            type="button"
                            id="button-addon2"
                        >
                            Search!
                        </button>
                    </div>
                </div>
            </div>
        </b-row>
        <b-row class="justify-content-md-center">
            <b-col cols="10">
                <b-button size="sm" block v-b-toggle.search-options variant="outline-primary"
                    >Options</b-button
                >
                <b-collapse id="search-options" class="mt-2"> </b-collapse
            ></b-col>
        </b-row>
        <card :profiles="this.profiles"></card>
        <b-row v-if="this.profiles !== null" class="justify-content-md-center">
            <b-col cols="12">
                <nav aria-label="Page navigation example">
                    <ul class="pagination">
                        <li class="page-item"><a class="page-link" href="#">Previous</a></li>
                        <li v-for="index in this.currentPage" :key="index" class="page-item">
                            <button type="button" @click="getProfiles(index)" class="page-link">
                                {{ index }}
                            </button>
                        </li>
                        <li class="page-item"><a class="page-link" href="#">Next</a></li>
                    </ul>
                </nav>
            </b-col>
        </b-row>
    </b-container>
</template>

<script>
import axios from 'axios';
import Card from './CardComponent';
export default {
    name: 'search',
    components: {
        Card,
    },
    data() {
        return {
            query: null,
            perPage: 20,
            currentPage: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            profiles: null,
        };
    },
    methods: {
        getProfiles(currentPage) {
            // TODO: Fix this
            if (!Number.isInteger(currentPage)) {
                currentPage = 1;
            }
            const path = `http://localhost:5000/api/1.0/profiles/${this.query}/${this.perPage}/${currentPage}`;
            axios
                .get(path)
                .then((res) => {
                    this.profiles = res.data;
                })
                .catch((error) => {
                    console.error(error);
                });
        },
    },
};
</script>

<style>
#search-wrapper {
    margin-top: 50px;
}
</style>
