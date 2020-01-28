# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

import mxnet as mx
from benchmark.opperf.utils.benchmark_utils import run_performance_test
from benchmark.opperf.utils.common_utils import merge_map_list
from benchmark.opperf.rules.default_params import MX_OP_MODULE

"""Performance benchmark tests for MXNet NDArray basic NN Operators.

1. FullyConnected
2. Dropout
3. BatchNorm

"""


def run_nn_basic_operators_benchmarks(ctx=mx.cpu(), dtype='float32', profiler='native', warmup=25, runs=100):
    # FullyConnnected operator benchmarks
    fc_benchmark_res = run_performance_test([getattr(MX_OP_MODULE, "FullyConnected")],
                                            run_backward=True,
                                            dtype=dtype,
                                            ctx=ctx,
                                            profiler=profiler,
                                            inputs=[{"data": (32, 3, 256, 256),
                                                     "num_hidden": 64,
                                                     "weight": (64, 3 * 256 * 256),
                                                     "bias": (64,),
                                                     "flatten": True},
                                                    {"data": (32, 3, 256, 256),
                                                     "num_hidden": 64,
                                                     "weight": (64, 256),
                                                     "bias": (64,),
                                                     "flatten": False}],
                                            warmup=warmup,
                                            runs=runs)

    # Dropout benchmarks
    dropout_benchmark_res = run_performance_test([getattr(MX_OP_MODULE, "Dropout")],
                                                 run_backward=True,
                                                 dtype=dtype,
                                                 ctx=ctx,
                                                 profiler=profiler,
                                                 inputs=[{"data": (32, 3, 256, 256),
                                                          "p": 0.5,
                                                          "mode": "always"},
                                                         {"data": (10000, 10),
                                                          "p": 0.5,
                                                          "mode": "always"}],
                                                 warmup=warmup,
                                                 runs=runs)
    # BatchNorm benchmarks
    batchnorm_benchmark_res = run_performance_test([getattr(MX_OP_MODULE, "BatchNorm")],
                                                   run_backward=True,
                                                   dtype=dtype,
                                                   ctx=ctx,
                                                   profiler=profiler,
                                                   inputs=[{"data": (32, 3, 256, 256),
                                                            "gamma": (3,),
                                                            "beta": (3,),
                                                            "moving_mean": (3,),
                                                            "moving_var": (3,)},
                                                           {"data": (32, 3, 10000, 10),
                                                            "gamma": (3,),
                                                            "beta": (3,),
                                                            "moving_mean": (3,),
                                                            "moving_var": (3,)}],
                                                   warmup=warmup,
                                                   runs=runs)
    # SoftmaxOutput benchmarks
    softmaxoutput_benchmark_res = run_performance_test([getattr(MX_OP_MODULE, "SoftmaxOutput")],
                                                   run_backward=True,
                                                   dtype=dtype,
                                                   ctx=ctx,
                                                   profiler=profiler,
                                                   inputs=[{"data": (32, 3, 256, 256),
                                                            "label": (32, 3, 256)},
                                                           {"data": (32, 3, 10000, 10),
                                                            "label": (32, 3, 10000),
                                                            "grad_scale": .5,
                                                            "normalization": 'batch'}],
                                                   warmup=warmup,
                                                   runs=runs)
    # LinearRegressionOutput, LogisticRegressionOutput, and MAERegressionOutput benchmarks
    regressionoutput_benchmark_res = run_performance_test([getattr(MX_OP_MODULE, "LinearRegressionOutput"),
                                                           getattr(MX_OP_MODULE, "LogisticRegressionOutput"),
                                                           getattr(MX_OP_MODULE, "MAERegressionOutput")],
                                                   run_backward=True,
                                                   dtype=dtype,
                                                   ctx=ctx,
                                                   profiler=profiler,
                                                   inputs=[{"data": (32, 3, 256, 256),
                                                            "label": (32, 3, 256, 256)},
                                                           {"data": (32, 3, 10000, 10),
                                                            "label": (32, 3, 10000, 10),
                                                            "grad_scale": .5}],
                                                   warmup=warmup,
                                                   runs=runs)
    # SVMOutput benchmarks
    svmoutput_benchmark_res = run_performance_test([getattr(MX_OP_MODULE, "SVMOutput")],
                                                   run_backward=True,
                                                   dtype=dtype,
                                                   ctx=ctx,
                                                   profiler=profiler,
                                                   inputs=[{"data": (32, 3, 256, 256),
                                                            "label": (32, 3, 256)},
                                                           {"data": (32, 3, 10000, 10),
                                                            "label": (32, 3, 10000),
                                                            "margin": .5,
                                                            "regularization_coefficient": .5}],
                                                   warmup=warmup,
                                                   runs=runs)
    # L2Normalization benchmarks
    l2_benchmark_res = run_performance_test([getattr(MX_OP_MODULE, "L2Normalization")],
                                                   run_backward=True,
                                                   dtype=dtype,
                                                   ctx=ctx,
                                                   profiler=profiler,
                                                   inputs=[{"data": (32, 3, 256, 256)},
                                                           {"data": (32, 3, 10000, 10),
                                                            "eps": .01}],
                                                   warmup=warmup,
                                                   runs=runs)
    # LayerNorm benchmarks
    layernorm_benchmark_res = run_performance_test([getattr(MX_OP_MODULE, "LayerNorm")],
                                                   run_backward=True,
                                                   dtype=dtype,
                                                   ctx=ctx,
                                                   profiler=profiler,
                                                   inputs=[{"data": (32, 3, 256, 256),
                                                            "gamma": (256,),
                                                            "beta": (256,)},
                                                           {"data": (32, 3, 10000, 10),
                                                            "gamma": (10,),
                                                            "beta": (10,),
                                                            "eps": .01}],
                                                   warmup=warmup,
                                                   runs=runs)
    # InstanceNorm benchmarks
    instancenorm_benchmark_res = run_performance_test([getattr(MX_OP_MODULE, "InstanceNorm")],
                                                   run_backward=True,
                                                   dtype=dtype,
                                                   ctx=ctx,
                                                   profiler=profiler,
                                                   inputs=[{"data": (32, 3, 256, 256),
                                                            "gamma": (3,),
                                                            "beta": (3,)},
                                                           {"data": (32, 3, 10000, 10),
                                                            "gamma": (3,),
                                                            "beta": (3,),
                                                            "eps": .01}],
                                                   warmup=warmup,
                                                   runs=runs)
    # Embedding benchmarks
    embedding_benchmark_res = run_performance_test([getattr(MX_OP_MODULE, "Embedding")],
                                                   run_backward=False,
                                                   dtype=dtype,
                                                   ctx=ctx,
                                                   profiler=profiler,
                                                   inputs=[{"data": (32, 3, 256, 256),
                                                            "weight": (3, 4),
                                                            "input_dim": 3,
                                                            "output_dim": 4},
                                                           {"data": (32, 3, 10000, 10),
                                                            "weight": (16, 9),
                                                            "input_dim": 16,
                                                            "output_dim": 9}],
                                                   warmup=warmup,
                                                   runs=runs)
    # Correlation benchmarks
    correlation_benchmark_res = run_performance_test([getattr(MX_OP_MODULE, "Correlation")],
                                                   run_backward=False,
                                                   dtype=dtype,
                                                   ctx=ctx,
                                                   profiler=profiler,
                                                   inputs=[{"data1": (32, 3, 256, 256),
                                                            "data2": (32, 3, 256, 256)},
                                                           {"data1": (32, 3, 10000, 10),
                                                            "data2": (32, 3, 10000, 10),
                                                            "kernel_size": 3,
                                                            "max_displacement": 2,
                                                            "stride1": 2,
                                                            "stride2": 2}],
                                                   warmup=warmup,
                                                   runs=runs)
    # Prepare combined results
    mx_basic_nn_results = merge_map_list(fc_benchmark_res + dropout_benchmark_res + batchnorm_benchmark_res + softmaxoutput_benchmark_res + regressionoutput_benchmark_res + svmoutput_benchmark_res + l2_benchmark_res + layernorm_benchmark_res + instancenorm_benchmark_res + embedding_benchmark_res + correlation_benchmark_res)
    return mx_basic_nn_results
