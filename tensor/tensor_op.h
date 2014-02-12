#ifndef CXXNET_TENSOR_OP_H
#define CXXNET_TENSOR_OP_H
/*!
 * \file tensor_op.h
 * \brief definitions of tensor operators
 *
 * \author Bing Hsu, Tianqi Chen
 */
#include "tensor.h"

namespace cxxnet {
    /*! \brief namespace for operators */
    namespace op {
        /*! \brief mul operator */
        struct mul{
            _XINLINE_ static real_t Map(real_t a, real_t b) {
                return a * b;
            }
        };
        /*! \brief plus operator */
        struct plus {
            _XINLINE_ static real_t Map(real_t a, real_t b) {
                return a + b;
            }        
        };
        /*! \brief minus operator */
        struct minus {
            _XINLINE_ static real_t Map(real_t a, real_t b) {
                return a - b;
            }
        };
        /*! \brief divide operator */
        struct div {
            _XINLINE_ static real_t Map(real_t a, real_t b) {
                return a / b;
            }        
        };
    }; // namespace op

    /*! \brief namespace for savers */
    namespace sv { 
        /*! \brief save to saver: = */
        struct saveto {
            _XINLINE_ static void Save(real_t& a, real_t b) {
                a  = b;
            }            
        };
        /*! \brief save to saver: += */
        struct addto {
            _XINLINE_ static void Save(real_t& a, real_t b) {
                a += b;
            }        
        };
        /*! \brief minus to saver: -= */
        struct minusto {
            _XINLINE_ static void Save(real_t& a, real_t b) {
                a -= b;
            }        
        };
        /*! \brief multiply to saver: *= */
        struct multo {
            _XINLINE_ static void Save(real_t& a, real_t b) {
                a *= b;
            }        
        };
        /*! \brief divide to saver: /= */
        struct divto {
            _XINLINE_ static void Save(real_t& a, real_t b) {
                a /= b;
            }  
        };
    }; // namespace sv
}; // namespace cxxnet
#endif // TENSOR_OP_H
