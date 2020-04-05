<template>
    <b-container id="search-wrapper">
        <b-row>
            <div class="input-group mb-3">
                <b-form-input
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
        </b-row>
        <card :profiles="this.profiles"></card>
        <div class="overflow-auto" v-if="this.profiles !== null">
            <div class="mt-3">
                <b-pagination
                    @input="getProfiles(currentPage)"
                    v-model="currentPage"
                    :total-rows="rows"
                    :per-page="perPage"
                    align="fill"
                ></b-pagination>
            </div>
        </div>
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
            rows: 900,
            perPage: 20,
            currentPage: 1,
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
